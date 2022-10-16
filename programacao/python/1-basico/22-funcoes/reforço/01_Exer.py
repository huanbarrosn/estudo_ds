
'''
Faça um programa para imprimir:
    1
    2   2
    3   3   3
    .....
    n   n   n   n   n   n  ... n
para um n informado pelo usuário. Use uma função que receba
um valor n inteiro e imprima até a n-ésima linha.
'''



def num(b):
    for i in range(1, b+1):
        print()
        for c in range(i):
            print(i, end=' ')


num(25)
