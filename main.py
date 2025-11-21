from grafo_loader import GrafoLoader
from rota_calculator import RotaCalculator
from mapa_visualizador import MapaVisualizador


def main(cidade, coord_origem, coord_destino):
    loader = GrafoLoader()
    grafo = loader.carregar_grafo(cidade)
    
    calculator = RotaCalculator(grafo)
    caminho = calculator.calcular_rota(coord_origem, coord_destino)
    coords_caminho = calculator.obter_coordenadas_caminho(caminho)
    distancia = calculator.calcular_distancia(caminho)
    
    return coords_caminho, distancia


if __name__ == "__main__":
    usar_exemplo = input("Deseja usar o exemplo pré-definido? (1 para sim, 0 para não):")

    if usar_exemplo == "1":
        cidade = "Campina Grande, Paraíba, Brazil"
        origem = (-7.2306, -35.8811)
        destino = (-7.2137, -35.9071)
    else:
        cidade = input("Digite a cidade (ex: Campina Grande, Paraíba, Brazil): ")
        
        lat_origem = float(input("Digite a latitude da origem: "))
        lon_origem = float(input("Digite a longitude da origem: "))
        origem = (lat_origem, lon_origem)
        
        lat_destino = float(input("Digite a latitude do destino: "))
        lon_destino = float(input("Digite a longitude do destino: "))
        destino = (lat_destino, lon_destino)
    
    coordenadas_caminho, distancia_total = main(cidade, origem, destino)
    print(f"Distância total: {distancia_total:.2f} km")
    print(f"Número de pontos no caminho: {len(coordenadas_caminho)}")
    
    visualizador = MapaVisualizador()
    visualizador.criar_mapa(origem)
    visualizador.adicionar_rota(coordenadas_caminho, distancia_total)
    visualizador.adicionar_marcadores(origem, destino)
    visualizador.salvar_mapa("rota.html")
