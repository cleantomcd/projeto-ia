import osmnx as ox

class GrafoLoader:
    """Carrega e salva grafos de uma cidade usando a biblioteca osmnx."""

    def __init__(self, network_type="drive"):
        """
        Inicializa o GrafoLoader.

        Parameters:
            network_type (str): Tipo de rede a ser carregada (ex.: 'drive').
        """
        self.network_type = network_type

    def carregar_grafo(self, cidade):
        """
        Carrega o grafo da cidade e salva como arquivo .gpickle.

        Parameters:
            cidade: Nome da cidade (ex.: 'Campina Grande, Paraíba, Brazil').

        Returns:
            networkx.MultiDiGraph: Grafo da cidade.
        """
        print("Carregando o grafo. AGUARDE...")
        grafo = ox.graph_from_place(cidade, network_type=self.network_type)
        ox.save_graphml(grafo, f"{cidade}.gpickle")
        return grafo
