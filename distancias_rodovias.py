import osmnx as ox
import networkx as nx
from geopy.distance import geodesic
import folium

# ==================== 1. CONFIGURAÇÕES E DADOS ====================

PONTOS_INTERESSE = {
    "Açude Velho": (-7.2294, -35.8819),
    "Parque do Povo": (-7.2306, -35.8811),
    "UFCG Campina Grande": (-7.2137, -35.9071)
}

LOCAL_CONFIG = {
    "query": "Campina Grande, Paraíba, Brazil",
    "network_type": "drive"
}

ARQUIVO_SAIDA = "rota_campina.html"

# ==================== 2. CARREGAMENTO DE DADOS ====================

def carregar_grafo(query, network_type):
    """Baixa o grafo de ruas do OpenStreetMap."""
    print(f"Baixando grafo real de '{query}'...")

    return ox.graph_from_place(query, network_type=network_type)

# ==================== 3. LÓGICA DE ROTA (A*) ====================

def calcular_rota_otima(G, pontos, nome_origem, nome_destino):
    """Calcula a rota A* entre dois pontos nomeados."""

    # Coordenadas dos pontos de interesse
    o_lat, o_lon = pontos[nome_origem]
    d_lat, d_lon = pontos[nome_destino]

    # Encontrar nós do grafo mais próximos às coordenadas reais
    origem_node = ox.distance.nearest_nodes(G, o_lon, o_lat)
    destino_node = ox.distance.nearest_nodes(G, d_lon, d_lat)

    # Definir heurística
    def heuristica(n1, n2):
        # Acesso aos dados dos nós n1 e n2 dentro de G
        node1 = G.nodes[n1]
        node2 = G.nodes[n2]
        return geodesic((node1['y'], node1['x']), (node2['y'], node2['x'])).km

    print(f"\nCalculando menor rota entre {nome_origem} e {nome_destino}...")

    # Algoritmo A* do NetworkX
    caminho = nx.astar_path(G, origem_node, destino_node, heuristic=heuristica, weight='length')

    # Calcular distância total
    distancia_km = sum(G[u][v][0]['length'] for u, v in zip(caminho[:-1], caminho[1:])) / 1000

    return caminho, distancia_km

# ==================== 4. VISUALIZAÇÃO ====================

def gerar_mapa(G, caminho, distancia, pontos, nome_origem, nome_destino):
    """Gera o mapa Folium com a rota e marcadores."""
    print("Gerando mapa interativo...")

    # Centralizar mapa
    mapa2 = folium.Map(location=[-7.24, -35.89], zoom_start=14)

    # Extrair coordenadas da rota para o PolyLine
    coords_rota = [(G.nodes[n]['y'], G.nodes[n]['x']) for n in caminho]

    # Desenhar Rota
    folium.PolyLine(
        coords_rota,
        color='red',
        weight=6,
        opacity=0.8,
        popup=f"Rota ótima ({distancia:,.2f} km)"
    ).add_to(mapa2)

    # Adicionar Marcadores
    for nome, (lat, lon) in pontos.items():
        if nome == nome_origem:
            cor = 'green'
        elif nome == nome_destino:
            cor = 'red'
        else:
            cor = 'blue'

        folium.Marker(
            location=(lat, lon),
            popup=f"<b>{nome}</b>",
            icon=folium.Icon(color=cor)
        ).add_to(mapa2)

    return mapa2

# ==================== 5. MAIN ====================

def main():
    # 1. Obter Grafo
    G = carregar_grafo(LOCAL_CONFIG["query"], LOCAL_CONFIG["network_type"])

    # 2. Definir paranaômetros da viagem
    origem = "Parque do Povo"
    destino = "UFCG Campina Grande"

    # 3. Calcular Caminho
    caminho, distancia = calcular_rota_otima(G, PONTOS_INTERESSE, origem, destino)
    print(f"Distância total: {distancia:,.2f} km")

    # 4. Gerar Mapa
    mapa2 = gerar_mapa(G, caminho, distancia, PONTOS_INTERESSE, origem, destino)

    # 5. Salvar e Retornar
    mapa2.save(ARQUIVO_SAIDA)
    print(f"\nMapa salvo como '{ARQUIVO_SAIDA}'")

    return mapa2

# Executa a main e exibe o mapa
if __name__ == "__main__":
    mapa2 = main()