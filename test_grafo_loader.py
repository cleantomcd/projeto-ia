import pytest
from unittest.mock import patch, MagicMock
from grafo_loader import GrafoLoader


def test_init_default():
    loader = GrafoLoader()
    assert loader.network_type == "drive"


@patch("grafo_loader.ox.save_graphml")
@patch("grafo_loader.ox.graph_from_place")
def test_carregar_grafo(mock_graph_from_place, mock_save_graphml):
    fake_graph = MagicMock()
    mock_graph_from_place.return_value = fake_graph
    loader = GrafoLoader(network_type="drive")
    cidade = "Campina Grande, Paraíba, Brazil"
    resultado = loader.carregar_grafo(cidade)

    assert resultado is fake_graph
    mock_graph_from_place.assert_called_once_with(cidade, network_type="drive")
    mock_save_graphml.assert_called_once_with(fake_graph, f"{cidade}.gpickle")
