


'''
Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado.
'''


def tamanho_int(num):
    num = str(num)
    return len(num)


a = tamanho_int(10)

print(f'O numero informado tem {a} dígitos.')
