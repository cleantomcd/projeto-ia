import folium

class MapaVisualizador:
    """Classe responsável por gerar e manipular mapas usando folium."""

    def __init__(self):
        """Inicializa o objeto sem mapa carregado."""
        self.mapa = None

    def criar_mapa(self, coord_centro, zoom=14):
        """
        Cria um mapa centralizado em uma coordenada.

        Parameters:
            coord_centro: Coordenada central (lat, lon)
            zoom: Nível de zoom inicial.

        Returns:
            folium.Map: Objeto de mapa criado.
        """
        self.mapa = folium.Map(location=coord_centro, zoom_start=zoom)
        return self.mapa

    def adicionar_rota(self, coords_rota, distancia):
        """
        Adiciona uma rota ao mapa como uma linha vermelha.

        Parameters:
            coords_rota: Lista de coordenadas da rota.
            distancia: Distância total em quilômetros.
        """
        folium.PolyLine(
            coords_rota,
            color="red",
            weight=6,
            opacity=0.8,
            popup=f"Rota ótima ({distancia:.2f} km)",
        ).add_to(self.mapa)

    def adicionar_marcadores(self, coord_origem, coord_destino):
        """
        Adiciona marcadores da origem e destino no mapa.

        Parameters:
            coord_origem: Coordenada da origem.
            coord_destino: Coordenada do destino.
        """
        folium.Marker(
            location=coord_origem, popup="Origem", icon=folium.Icon(color="green")
        ).add_to(self.mapa)

        folium.Marker(
            location=coord_destino, popup="Destino", icon=folium.Icon(color="red")
        ).add_to(self.mapa)

    def salvar_mapa(self, arquivo):
        """
        Salva o mapa em um arquivo HTML.

        Parameters:
            arquivo (str): Nome do arquivo.
        """
        self.mapa.save(arquivo)
