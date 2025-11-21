import osmnx as ox


class GrafoLoader:
    def __init__(self, network_type="drive"):
        self.network_type = network_type
    
    def carregar_grafo(self, cidade):
        print("Carregando o grafo. AGUARDE")
        grafo = ox.graph_from_place(cidade, network_type=self.network_type)
        ox.save_graphml(grafo, f"{cidade}.gpickle")
        return grafo