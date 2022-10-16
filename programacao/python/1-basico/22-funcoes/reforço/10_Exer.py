
'''
Jogo de Craps.
Faça um programa de implemente um jogo de Craps. O jogador lança um par de dados, obtendo um
valor entre 2 e 12. Se, na primeira jogada, você tirar 7 ou 11, você um "natural" e ganhou.

Se você tirar 2, 3 ou 12 na primeira jogada, isto é chamado de "craps" e você perdeu.
Se, na primeira jogada, você fez um 4, 5, 6, 8, 9 ou 10,este é seu "Ponto".
Seu objetivo agora é continuar jogando os dados até tirar este número novamente.
Você perde, no entanto, se tirar um 7 antes de tirar este Ponto novamente.
'''

from random import *


def sorteio_dados():
    dado1 = randint(1, 6)
    dado2 = randint(1, 6)
    return dado1+dado2


ganhou = [7, 11]
perdeu = [2, 3, 12]

a = sorteio_dados()

if a in ganhou:
    print(f'NATURAL, você tirou {a} no dado e ganhou.')

elif a in perdeu:
    print(f'CRAPS, você tirou {a} no dado e perdeu.')


print(f'Você tirou {a} no dado e precisa tirar {a} novamente para ganhar.')
while True:
    b = sorteio_dados()

    if b == 7:
        print(f'GAME OVER, você tirou {b} no dado e perdeu.')
        break
    if b == a:
        print(f'Parabéns, você tirou {b} no dado novamente e ganhou.')
        break





