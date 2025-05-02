Análise de Dados das Cartas do Clash Royale
Este script em Python, utilizando a biblioteca pandas, realiza uma análise detalhada de desempenho das cartas do jogo Clash Royale, com base em um arquivo CSV chamado clash_royale.csv. O objetivo é filtrar e destacar conjuntos específicos de cartas com base em sua taxa de vitória, uso e variações de desempenho.


🧪 Etapas do processamento:
Leitura e preparação dos dados:
O arquivo clash_royale.csv é carregado em um DataFrame.
As colunas são renomeadas para nomes mais descritivos e em português, como "Carta", "Taxa de vitória", "Uso", entre outras.



mascara_10melhores_carta: Seleciona as 10 cartas com maior taxa de vitória, acima de 55%, e com crescimento positivo nessa taxa (mudança > 1).

mascara_10piores_cartas: Filtra as 10 cartas com pior desempenho, com taxa de vitória abaixo de 50% e queda na taxa de vitória (mudança < -0.1).

mascara_cartas_mais_usadas: Aponta as 10 cartas mais utilizadas pelos jogadores (uso > 5%).

mascara_cartas_menos_usadas: Destaca as 10 cartas menos utilizadas (uso < 1%).

mascara_cartas_mais_usadas_menor_winrate: Cartas muito usadas, mas com taxa de vitória inferior a 50% — indicam possíveis armadilhas na escolha de decks.

mascara_cartas_menos_usadas_maior_winrate: Cartas pouco usadas, mas com alto desempenho (taxa de vitória > 50%) — potenciais pérolas ocultas.

cartas_armadilhas: Uma lista de 10 cartas muito populares, porém com as piores taxas de vitória.

perolas_ocultas: Seleciona cartas pouco usadas, mas com taxa de vitória acima de 55%, indicando opções fortes e subestimadas.
