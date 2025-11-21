import osmnx as ox
import networkx as nx
from geopy.distance import geodesic


class RotaCalculator:
    def __init__(self, grafo):
        self.grafo = grafo
    
    def calcular_rota(self, coord_origem, coord_destino):
        origem_node = ox.distance.nearest_nodes(self.grafo, coord_origem[1], coord_origem[0])
        destino_node = ox.distance.nearest_nodes(self.grafo, coord_destino[1], coord_destino[0])
        
        def heuristica(n1, n2):
            node1 = self.grafo.nodes[n1]
            node2 = self.grafo.nodes[n2]
            return geodesic((node1['y'], node1['x']), (node2['y'], node2['x'])).km
        
        caminho = nx.astar_path(self.grafo, origem_node, destino_node, heuristic=heuristica, weight='length')
        return caminho
    
    def obter_coordenadas_caminho(self, caminho):
        return [(self.grafo.nodes[n]['y'], self.grafo.nodes[n]['x']) for n in caminho]
    
    def calcular_distancia(self, caminho):
        return sum(self.grafo[u][v][0]['length'] for u, v in zip(caminho[:-1], caminho[1:])) / 1000
