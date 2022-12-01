'''
Quadrado mágico.
Um quadrado mágico é aquele dividido em linhas e colunas, com um número em cada
posição e no qual a soma das linhas, colunas e diagonais é a mesma. Por exemplo, veja um quadrado
mágico de lado 3, com números de 1 a 9:

8  3  4
1  5  9
6  7  2

Elabore uma função que identifica e mostra na tela todos os quadrados mágicos com as características acima.
Dica: produza todas as combinações possíveis e verifique a soma quando completar cada quadrado.
Usar um vetor de 1 a 9 parece ser mais simples que usar uma matriz 3x3.
'''

from random import *

possibilidades = []
quadrados = []

f = 9
for i in range(9, 1, -1):
    f = f * (i - 1)

a = 'certo'
cont = 1

while True:
    matriz = sample(range(1, 10), 9)

    # adicionando as matrizes
    if matriz not in possibilidades:
        possibilidades.append(matriz)
        print(f'volta {cont}')
        cont += 1
    else:
        continue

    # verificando as linhas
    if not sum(matriz[0:3]) == sum(matriz[3:6]) == sum(matriz[6:9]) == 15:
        continue

    # verificando as colunas
    for i in range(3):
        c = [x for x in matriz[i::3]]
        if not sum(c) == 15:
            a = 'erro'
    if a == 'erro':
        continue

    # verificando as diagonais
    d1 = [x for x in matriz[::4]]
    d2 = [y for y in matriz[2:-2:2]]
    if not sum(d1) == sum(d2) == 15:
        continue

    quadrados.append(matriz)
    print(f'\033[31m{matriz}\033[m')

    # pausa
    if len(possibilidades) == f:
        break
