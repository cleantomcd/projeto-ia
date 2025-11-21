import folium


class MapaVisualizador:
    def __init__(self):
        self.mapa = None
    
    def criar_mapa(self, coord_centro, zoom=14):
        self.mapa = folium.Map(location=coord_centro, zoom_start=zoom)
        return self.mapa
    
    def adicionar_rota(self, coords_rota, distancia):
        folium.PolyLine(
            coords_rota,
            color='red',
            weight=6,
            opacity=0.8,
            popup=f"Rota ótima ({distancia:.2f} km)"
        ).add_to(self.mapa)
    
    def adicionar_marcadores(self, coord_origem, coord_destino):
        folium.Marker(
            location=coord_origem,
            popup="Origem",
            icon=folium.Icon(color='green')
        ).add_to(self.mapa)
        
        folium.Marker(
            location=coord_destino,
            popup="Destino",
            icon=folium.Icon(color='red')
        ).add_to(self.mapa)
    
    def salvar_mapa(self, arquivo):
        self.mapa.save(arquivo)
