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


def valida(num):
        
    if '.' in num:
        if num.index('.') == 0:
            return True
                
    num = num.replace('.','')
        
    if not num.isdigit():
        return True
  
    
def loop(y):
    while valida(y):
        print('Erro. Digite um numero inteiro ou racional.')
        y = input('\nDigite o valor: ')
    return float(y)
    
def resumo(valor,aumento,corte):
    valor = loop(valor)
    print(f'\nPreco analisado: {"":>3}{formata(valor)}')
    print(f'Dobro do preco: {"":>4}{dobro_real(valor)}')
    print(f'Metade do preco: {"":>3}{metade_real(valor)}')
    print(f'{aumento}% de aumento: {"":>4}{aumento_real(valor,aumento)}')
    print(f'{corte}% de corte: {"":>6}{diminuir_real(valor,corte)}')