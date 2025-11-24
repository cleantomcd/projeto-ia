import pytest
from unittest.mock import patch, MagicMock
from mapa_visualizador import MapaVisualizador

@patch("mapa_visualizador.folium.Map")
def test_criar_mapa(mock_map):
    instancia_map = MagicMock()
    mock_map.return_value = instancia_map
    mv = MapaVisualizador()
    mapa = mv.criar_mapa(coord_centro = (-7.1000, -34.8000), zoom = 14)

    mock_map.assert_called_once_with(
        location = (-7.1000, -34.8000),
        zoom_start = 14
    )

    assert mapa == instancia_map
    assert mv.mapa == instancia_map

@patch("mapa_visualizador.folium.PolyLine")
def test_adicionar_rota(mock_polyline):
    mv = MapaVisualizador()
    mv.mapa = MagicMock() 

    instancia_poly = MagicMock()
    mock_polyline.return_value = instancia_poly
    coords = [(-7.1000, -34.8000), (-7.2500, -34.9000)]
    mv.adicionar_rota(coords, distancia=2.5)

    mock_polyline.assert_called_once_with(
        coords,
        color = "red",
        weight = 6,
        opacity = 0.8,
        popup = "Rota ótima (2.50 km)"
    )

    instancia_poly.add_to.assert_called_once_with(mv.mapa)

@patch("mapa_visualizador.folium.Marker")
@patch("mapa_visualizador.folium.Icon")
def test_adicionar_marcadores(mock_icon, mock_marker):
    mv = MapaVisualizador()
    mv.mapa = MagicMock()

    icon_green = MagicMock()
    icon_red = MagicMock()
    mock_icon.side_effect = [icon_green, icon_red]

    marker_origem = MagicMock()
    marker_destino = MagicMock()
    mock_marker.side_effect = [marker_origem, marker_destino]

    mv.adicionar_marcadores(
        coord_origem=(-7.1000, -34.8000),
        coord_destino=(-7.2500, -34.9000)
    )

    mock_icon.assert_any_call(color='green')
    mock_marker.assert_any_call(
        location=(-7.1000, -34.8000),
        popup="Origem",
        icon=icon_green
    )
    marker_origem.add_to.assert_called_once_with(mv.mapa)

    mock_icon.assert_any_call(color='red')
    mock_marker.assert_any_call(
        location=(-7.2500, -34.9000),
        popup="Destino",
        icon=icon_red
    )
    marker_destino.add_to.assert_called_once_with(mv.mapa)

def test_salvar_mapa():
    mv = MapaVisualizador()
    mv.mapa = MagicMock()

    mv.salvar_mapa("arquivo.html")
    mv.mapa.save.assert_called_once_with("arquivo.html")
