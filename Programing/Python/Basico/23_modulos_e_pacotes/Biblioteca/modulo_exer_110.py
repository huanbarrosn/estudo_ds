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

def resumo(valor,aumento,corte):
    print(f'Preco analisado: {formata(valor):>10}')
    print(f'Dobro do preco: {dobro_real(valor):>11}')
    print(f'Metade do preco: {metade_real(valor):>9}')
    print(f'{aumento}% de aumento: {aumento_real(valor,aumento):>11}')
    print(f'{corte}% de corte: {diminuir_real(valor,corte):>12}')

