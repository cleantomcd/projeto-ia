import time
import random
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from grafo_loader import GrafoLoader
from rota_calculator import RotaCalculator

gl = GrafoLoader()    
G = gl.carregar_grafo("Campina Grande, Paraíba, Brazil")
rc = RotaCalculator(G)

def gerar_coordenadas():
    lat_min, lat_max = -7.26, -7.20
    lon_min, lon_max = -35.93, -35.87
    
    latitude = random.uniform(lat_min, lat_max)
    longitude = random.uniform(lon_min, lon_max)
    
    return latitude, longitude

def test_tempo():
    c1 = gerar_coordenadas()  
    c2 = gerar_coordenadas()
    rc.calcular_rota(c1,c2)

rep = 600

print("\nExecutando testes...\n")
tempos = []

for i in range(rep):
    ini = time.perf_counter()
    test_tempo()
    fim = time.perf_counter()
    tempos.append(fim-ini)

tempo_medio = sum(tempos)/rep
tempo_max = max(tempos)
tempo_min = min(tempos)

#desvio padrão tempo
aux = 0
for e in tempos:
    aux += (e - tempo_medio)**2
dp_tempo = (aux/len(tempos))**(0.5)
print("desvio  ",dp_tempo  )
z_tempo = (1.96*dp_tempo)/(rep**0.5)

ic_tempo = [tempo_medio-z_tempo,tempo_medio+z_tempo]

print("Resultados Obtidos:")
print(f"Grafo com {G.number_of_nodes()} nós | {rep} execuções")
print("        |  Média |   Max     |  Min  |  IC 95%")
print(f"Tempo   |  {tempo_medio:.4f}  |   {tempo_max:.4f}   |  {tempo_min:.4f}  |  [{ic_tempo[0]:.4f}, {ic_tempo[1]:.4f}]")

dados = np.array(tempos)
plt.hist(dados, bins=20, density=True)
x = np.linspace(min(dados), max(dados), 200)
y = norm.pdf(x, tempo_medio, dp_tempo)

plt.plot(x, y)
plt.title("Histograma com Curva Normal Ajustada")
plt.xlabel("Tempo de execução")
plt.ylabel("Densidade")
plt.show()
