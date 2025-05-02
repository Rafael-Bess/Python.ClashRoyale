import pandas as pd

df = pd.read_csv('clash_royale.csv')

df.rename(columns={ 'Card': 'Carta',
                    'id': 'ID',
                    'maxLevel': 'Nivel maximo',
                    'elixirCost': 'Custo de elixir',
                    'rarity': 'Raridade',
                    'Win Rate': 'Taxa de vitoria',
                    'Win Rate Change': 'Mudanca na taxa de vitoria',
                    'Usage': 'Uso',
                    'Usage Change': 'Mudanca no uso'}, inplace=True)

mascara_10melhores_carta = df[
    (df['Taxa de vitoria'] > 55) & (df['Mudanca na taxa de vitoria'] > 1) 
].nlargest(10, 'Taxa de vitoria')

mascara_10piores_cartas = df[
    (df['Taxa de vitoria'] < 50) & (df['Mudanca na taxa de vitoria'] < -0.1) 
].nsmallest(10, 'Taxa de vitoria')

mascara_cartas_mais_usadas = df[(df['Uso'] > 5)].nlargest(10, 'Uso')

mascara_cartas_menos_usadas = df[(df['Uso'] < 1)].nsmallest(10, 'Uso')

mascara_cartas_mais_usadas_menor_winrate = df[
    (df['Uso'] > 5) & (df['Taxa de vitoria'] < 50)
].nlargest(10, 'Taxa de vitoria')

mascara_cartas_menos_usadas_maior_winrate = df[
    (df['Uso'] < 1) & (df['Taxa de vitoria'] > 50)
].nlargest(10, 'Taxa de vitoria')

cartas_armadilhas = df[
    (df['Uso'] > 5) & (df['Taxa de vitoria'] < 50)
].nsmallest(10, 'Taxa de vitoria')

perolas_ocultas = df[
    (df['Uso'] < 5) & (df['Taxa de vitoria'] > 55)
].nlargest(10, 'Taxa de vitoria')


