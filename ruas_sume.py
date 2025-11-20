import osmnx as ox

# Baixe a rede de ruas para todo o Sumé
place = "Sumé, Brazil"
G_DF = ox.graph.graph_from_place(place, network_type='drive', simplify=False, retain_all=False, truncate_by_edge=False, which_result=None, custom_filter=None)

# Salve a rede para um arquivo .graphml
ox.save_graphml(G_DF, filepath="sume.graphml")

# Carregar a rede leve
G = ox.load_graphml("sume.graphml")

# Plotar o mapa
ox.plot_graph(G)