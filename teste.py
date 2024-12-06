import requests
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

# Função para obter a lista de todos os Pokémon
def fetch_all_pokemon():
    url = "https://pokeapi.co/api/v2/pokemon?limit=10000"  # Garantir que busca todos os Pokémon
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return [pokemon["name"] for pokemon in data["results"]]
    else:
        print(f"Erro ao buscar lista de Pokémon: {response.status_code}")
        return []

# Função para obter dados detalhados de um Pokémon pela API
def fetch_pokemon_data(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Erro ao buscar Pokémon {pokemon_name}: {response.status_code}")
        return None

# Obter lista de todos os Pokémon
pokemon_list = fetch_all_pokemon()
print(f"Total de Pokémon encontrados: {len(pokemon_list)}")

# Coletar dados de todos os Pokémon
data = []
for pokemon in pokemon_list:
    pokemon_data = fetch_pokemon_data(pokemon)
    if pokemon_data:
        data.append({
            "name": pokemon_data["name"],
            "height": pokemon_data["height"],  # altura em decímetros
            "weight": pokemon_data["weight"]   # peso em hectogramas
        })

# Criar DataFrame com os dados coletados
df = pd.DataFrame(data)
df_menor_pesado = df["weight"].min()
print(df)

'''
# Remover Pokémon sem peso ou altura válidos (caso existam)
df = df[(df["height"] > 0) & (df["weight"] > 0)]

# Calcular a correlação de Pearson
correlation, _ = pearsonr(df["height"], df["weight"])
print(f"Coeficiente de Correlação de Pearson: {correlation:.2f}")

# Criar o gráfico de dispersão
plt.figure(figsize=(10, 6))
plt.scatter(df["height"], df["weight"], color="blue", alpha=0.5)
plt.title("Correlação entre Altura e Peso de Todos os Pokémon")
plt.xlabel("Altura (dm)")
plt.ylabel("Peso (hg)")
plt.grid(True)

# Adicionar o coeficiente de correlação ao gráfico
plt.text(
    min(df["height"]), max(df["weight"]), 
    f"r = {correlation:.2f}", fontsize=12, color="red"
)

# Exibir o gráfico
plt.show()
'''
