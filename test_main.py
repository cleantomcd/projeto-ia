import pytest
from unittest.mock import patch, MagicMock
from main import main


@patch("main.GrafoLoader")
@patch("main.RotaCalculator")
def test_main(mock_rota_calc_class, mock_loader_class):
    mock_loader = MagicMock()
    mock_grafo = MagicMock()
    mock_loader.carregar_grafo.return_value = mock_grafo
    mock_loader_class.return_value = mock_loader

    mock_calc = MagicMock()
    mock_calc.calcular_rota.return_value = [1, 2, 3]
    mock_calc.obter_coordenadas_caminho.return_value = [
        (-7.1000, -34.8000),
        (-7.2000, -34.8500),
        (-7.2500, -34.9000),
    ]
    mock_calc.calcular_distancia.return_value = 0.25
    mock_rota_calc_class.return_value = mock_calc

    coords, dist = main(
        cidade="Campina Grande, Paraíba, Brazil",
        coord_origem=(-7.1000, -34.8000),
        coord_destino=(-7.2000, -34.8500),
    )

    mock_loader.carregar_grafo.assert_called_once_with(
        "Campina Grande, Paraíba, Brazil"
    )
    mock_calc.calcular_rota.assert_called_once()
    mock_calc.obter_coordenadas_caminho.assert_called_once_with([1, 2, 3])
    mock_calc.calcular_distancia.assert_called_once_with([1, 2, 3])
    assert coords == [(-7.1000, -34.8000), (-7.2000, -34.8500), (-7.2500, -34.9000)]
    assert dist == 0.25
