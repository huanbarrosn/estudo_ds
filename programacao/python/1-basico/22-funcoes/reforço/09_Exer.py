

'''
Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado.
Por exemplo: 127 -> 721.
'''


def reverso_int(num):
    num = str(num)
    num = num[::-1]

    return int(num)


a = reverso_int(1004)
print(f'O numero ao contrário fica {a}.')