import pytest
import networkx as nx
from unittest.mock import patch
from rota_calculator import RotaCalculator


@pytest.fixture
def mock_graph():
    G = nx.MultiDiGraph()
    G.add_node(1, y=-7.1000, x=-34.8000)
    G.add_node(2, y=-7.2000, x=-34.8500)
    G.add_node(3, y=-7.2500, x=-34.9000)

    G.add_edge(1, 2, length=100)
    G.add_edge(2, 3, length=150)

    return G


def test_obter_coordenadas_caminho(mock_graph):
    rota = RotaCalculator(mock_graph)
    caminho = [1, 2, 3]
    coords = rota.obter_coordenadas_caminho(caminho)
    assert coords == [(-7.1000, -34.8000), (-7.2000, -34.8500), (-7.2500, -34.9000)]


def test_calcular_distancia(mock_graph):
    rota = RotaCalculator(mock_graph)
    caminho = [1, 2, 3]
    distancia = rota.calcular_distancia(caminho)
    assert distancia == 0.25


def test_calcular_distancia_caminho_vazio(mock_graph):
    rota = RotaCalculator(mock_graph)
    assert rota.calcular_distancia([]) == 0


def test_calcular_distancia_um_no(mock_graph):
    rota = RotaCalculator(mock_graph)
    assert rota.calcular_distancia([1]) == 0


@patch("rota_calculator.ox.distance.nearest_nodes")
@patch("rota_calculator.nx.astar_path")
def test_calcular_rota(mock_astar, mock_nearest, mock_graph):
    mock_nearest.side_effect = [1, 3]
    mock_astar.return_value = [1, 2, 3]
    rota = RotaCalculator(mock_graph)
    caminho = rota.calcular_rota(
        coord_origem=(-7.1000, -34.8000), coord_destino=(-7.2500, -34.9000)
    )

    assert caminho == [1, 2, 3]
    assert mock_nearest.call_count == 2
    mock_astar.assert_called_once()


@patch(
    "rota_calculator.ox.distance.nearest_nodes",
    side_effect=ValueError("coordenadas inválidas"),
)
def test_calcular_rota_coordenadas_invalidas(mock_nearest, mock_graph):
    rota = RotaCalculator(mock_graph)
    with pytest.raises(ValueError):
        rota.calcular_rota((None, None), (None, None))


@patch("rota_calculator.ox.distance.nearest_nodes")
@patch("rota_calculator.nx.astar_path")
def test_calcular_rota_origem_igual_destino(mock_astar, mock_nearest, mock_graph):
    mock_nearest.side_effect = [1, 1]
    mock_astar.return_value = [1]
    rota = RotaCalculator(mock_graph)
    caminho = rota.calcular_rota(
        coord_origem=(-7.1000, -34.8000), coord_destino=(-7.1000, -34.8000)
    )

    assert caminho == [1]
    assert mock_nearest.call_count == 2
    mock_astar.assert_called_once()


@patch("rota_calculator.ox.distance.nearest_nodes")
@patch("rota_calculator.nx.astar_path")
def test_calcular_rota_heuristica(mock_astar, mock_nearest, mock_graph):
    mock_nearest.side_effect = [1, 3]

    def fake_astar(G, origem, destino, heuristic, weight):
        h = heuristic(origem, destino)
        assert isinstance(h, float)
        return [1, 2, 3]

    mock_astar.side_effect = fake_astar
    rota = RotaCalculator(mock_graph)
    caminho = rota.calcular_rota(
        coord_origem=(-7.1000, -34.8000), coord_destino=(-7.2500, -34.9000)
    )
    assert caminho == [1, 2, 3]
