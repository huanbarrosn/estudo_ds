def formata(x):
    x = f'{x:.2f}'
    x = x.replace('.', ',')
    return f'R${x}'


def metade_real(num):
    num /= 2
    return formata(num)


def dobro_real(num):
    num *= 2
    return formata(num)


def aumento_real(num,taxa):
    num *= 1+(taxa/100)
    return formata(num)


def diminuir_real(num,taxa):
    tx = num * (taxa/100)
    num = num-tx
    return formata(num)

'''
print(dobro_real(100))
print(metade_real(100))
print(aumento_real(100,10))
print(diminuir_real(100,10))
'''