

""" 

Exercício Python 104: Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante 
a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.

"""

def leia_int(x):

    number = input(x)

    while not number.isdigit():
        print('\033[31mErro. Digite um numero inteiro válido.\033[m')
        number = input(x)

    return int(number)

a = leia_int('Digite um número: ')
print(f'Você acabou de digitar o número {a}.')