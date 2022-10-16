
'''
Faça um programa para imprimir:

    1
    1   2
    1   2   3
    .....
    1   2   3   ...  n

para um n informado pelo usuário. Use uma função
que receba um valor n inteiro imprima até a n-ésima linha.
'''

def sequencia(b):
    for i in range(1, b+1):
        print()
        for x in range(i):
            print(x+1, end=' ')

sequencia(25)
