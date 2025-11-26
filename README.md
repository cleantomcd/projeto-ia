# Calculador de Rotas 🗺️

Sistema inteligente para cálculo de rotas otimizadas utilizando algoritmo A* (A-Star) com dados reais do OpenStreetMap e visualização interativa em mapas web.

## 📋 Sobre o Projeto

Este projeto implementa um sistema completo de planejamento de rotas que:

- **Utiliza dados reais**: Integração com OpenStreetMap para obter malha viária real das cidades
- **Algoritmo A***: Implementação do algoritmo A* (A-Star) para encontrar o caminho mais eficiente
- **Heurística geodésica**: Usa distância geodésica real como função heurística para otimização
- **Visualização interativa**: Gera mapas HTML interativos com a rota calculada
- **Arquitetura modular**: Código organizado em classes especializadas para fácil manutenção
- **Interface amigável**: Sistema de input interativo para facilitar o uso

## 🎯 Funcionalidades

- ✅ Cálculo de rotas otimizadas entre dois pontos geográficos
- ✅ Suporte a qualquer cidade disponível no OpenStreetMap
- ✅ Visualização da rota em mapa interativo
- ✅ Cálculo preciso de distâncias totais
- ✅ Marcadores de origem e destino
- ✅ Exportação do mapa em formato HTML
- ✅ Sistema modular e extensível

## 🏗️ Arquitetura do Sistema

O projeto segue os princípios SOLID com separação clara de responsabilidades:

### 📁 Estrutura dos Arquivos

#### `grafo_loader.py`
**Responsabilidade**: Carregamento de dados geográficos
- Classe `GrafoLoader` para obter grafos do OpenStreetMap
- Configuração de tipos de rede (drive, walk, bike)
- Otimização de carregamento de dados

#### `rota_calculator.py` 
**Responsabilidade**: Motor de cálculo de rotas
- Classe `RotaCalculator` com algoritmo A* otimizado
- Heurística geodésica para estimativa de distâncias
- Conversão de nós em coordenadas geográficas
- Cálculo preciso de distâncias totais

#### `mapa_visualizador.py`
**Responsabilidade**: Visualização e interface gráfica
- Classe `MapaVisualizador` para mapas interativos
- Geração de rotas visuais com Folium
- Sistema de marcadores personalizáveis
- Exportação para HTML responsivo

#### `main.py`
**Responsabilidade**: Orquestração e interface do usuário
- Coordenação entre todos os módulos
- Interface interativa para entrada de dados
- Fluxo principal de execução
- Tratamento de inputs do usuário



## 🚀 Como Usar

### Instalação das Dependências

```bash
# Criar e ativar ambiente virtual
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate     # Windows

# Instalar dependências
pip install -r requirements.txt
```

### Execução Interativa

```bash
# Executar interface interativa
python main.py
```

O programa solicitará:
1. **Nome da cidade** (ex: "São Paulo, São Paulo, Brazil")
2. **Coordenadas de origem** (latitude, longitude)  
3. **Coordenadas de destino** (latitude, longitude)

### Uso Programático

```python
from grafo_loader import GrafoLoader
from rota_calculator import RotaCalculator
from mapa_visualizador import MapaVisualizador

# 1. Carregar grafo da cidade
loader = GrafoLoader()
grafo = loader.carregar_grafo("Campina Grande, Paraíba, Brazil")

# 2. Calcular rota otimizada
calculator = RotaCalculator(grafo)
caminho = calculator.calcular_rota((-7.2306, -35.8811), (-7.2137, -35.9071))
coords_caminho = calculator.obter_coordenadas_caminho(caminho)
distancia = calculator.calcular_distancia(caminho)

# 3. Visualizar resultado
visualizador = MapaVisualizador()
visualizador.criar_mapa((-7.2306, -35.8811))
visualizador.adicionar_rota(coords_caminho, distancia)
visualizador.adicionar_marcadores((-7.2306, -35.8811), (-7.2137, -35.9071))
visualizador.salvar_mapa("minha_rota.html")
```

### Exemplo Pronto



```bash
# Executar exemplo com dados de Campina Grande
python distancias_rodovias.py
```
# Dados Estatisticos
### Distribuição do tempo de execução (população com distribuição normal):
<img width="1366" height="653" alt="grafico2" src="https://github.com/user-attachments/assets/e7d5612d-180a-47da-86d2-a362a54513f3" />
<img width="1366" height="653" alt="Figure_1" src="https://github.com/user-attachments/assets/13a176d7-7c2c-4304-847d-640a7dd701f5" />

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

