
'''

Exercício Python 106: faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o
comando e o manual vai aparecer. Quando o usuário digitar a palavra 'FIM', o programa se encerrará.
Importante: use cores.

'''



def colorir(msg,cor,tipo=0):
    cores = {
        'cinza':        '\033[1;97;100m',
        'vermelho':     '\033[1;97;101m',
        'verde':        '\033[1;97;102m',
        'amarelo':      '\033[1;97;103m',
        'azul':         '\033[1;97;104m',
        'magenta':      '\033[1;97;105m',
        'ciano':        '\033[1;97;106m',
        'branco':       '\033[1;97;107m'}


    print(cores[cor], end='')
    print('~' * 100)
    if tipo == 1:
        help(msg)
    else:
        print(msg)
    print('~' * 100)
    print('\033[m', end='')


def ajuda():

    while True:
        print()
        colorir('SISTEMA DE AJUDA PyHELP','magenta')
        com = input('Biblioteca ou projeto_1 >> ').casefold()
        if com == 'fim':
            break
        colorir(f'Acessando o manual do comando <{com}>', 'magenta')
        colorir(com,'vermelho',1)


ajuda()
