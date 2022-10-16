


"""

Exercício Python 103: Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros
opcionais: o nome de um jogador e quantos gols ele marcou.
O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.

"""


def futebol(nome='<Desconhecido>', gol='0'):
    if not nome.isalpha():
        nome = '<Desconhecido>'
    if not gol.isdigit():
        gol = '0'

    return f'\nO jogador {nome} fez {gol} gols (s) no campeonato'


nome_atleta = input('Nome do atleta: ').strip()
gols = input('Numero de gols: ').strip()

print(futebol(nome_atleta, gols))
