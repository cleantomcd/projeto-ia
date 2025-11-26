"""
Módulo responsável pelo cálculo de rotas utilizando um grafo
obtido pela biblioteca osmnx. Também fornece métodos auxiliares
para obtenção de coordenadas e cálculo de distância total.
"""

import osmnx as ox
import networkx as nx
from geopy.distance import geodesic


class RotaCalculator:
    """Calcula rotas ótimas em um grafo e fornece utilitários de análise."""

    def __init__(self, grafo):
        """
        Inicializa o calculador de rotas.

        Parameters:
            grafo (networkx.MultiDiGraph): Grafo carregado pelo OSMnx.
        """
        self.grafo = grafo

    def calcular_rota(self, coord_origem, coord_destino):
        """
        Calcula a rota ótima entre duas coordenadas usando A*.

        Parameters:
            coord_origem: Coordenadas de origem (lat, lon).
            coord_destino: Coordenadas de destino (lat, lon).

        Returns:
            list: Lista de nós representando o caminho encontrado.
        """
        origem_node = ox.distance.nearest_nodes(
            self.grafo, coord_origem[1], coord_origem[0]
        )
        destino_node = ox.distance.nearest_nodes(
            self.grafo, coord_destino[1], coord_destino[0]
        )

        def heuristica(n1, n2):
            """Heurística geodésica para o algoritmo A*."""
            node1 = self.grafo.nodes[n1]
            node2 = self.grafo.nodes[n2]
            return geodesic((node1["y"], node1["x"]),
                            (node2["y"], node2["x"])).km

        caminho = nx.astar_path(
            self.grafo,
            origem_node,
            destino_node,
            heuristic=heuristica,
            weight="length",
        )
        return caminho

    def obter_coordenadas_caminho(self, caminho):
        """
        Converte uma lista de nós em coordenadas geográficas.

        Parameters:
            caminho: Lista de ids de nós.

        Returns:
            list: Lista de tuplas (latitude, longitude).
        """
        return [
            (self.grafo.nodes[n]["y"], self.grafo.nodes[n]["x"])
            for n in caminho
        ]

    def calcular_distancia(self, caminho):
        """
        Calcula a distância total percorrida ao longo do caminho.

        Parameters:
            caminho: Lista de nós na ordem do percurso.

        Returns:
            float: Distância total em quilômetros.
        """
        return (
            sum(
                self.grafo[u][v][0]["length"]
                for u, v in zip(caminho[:-1], caminho[1:])
            )
            / 1000
        )
