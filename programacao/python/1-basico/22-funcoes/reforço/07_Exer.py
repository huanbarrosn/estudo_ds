'''
Faça um programa que use a função valorPagamento para
determinar o valor a ser pago por uma prestação de uma conta.

O programa deverá solicitar ao usuário o valor da prestação e
o número de dias em atraso e passar estes valores para a função
valorPagamento, que calculará o valor a ser pago e devolverá
este valor ao programa que a chamou. O programa deverá então
exibir o valor a ser pago na tela. Após a execução o programa
deverá voltar a pedir outro valor de prestação e assim
continuar até que seja informado um valor igual a zero para
a prestação. Neste momento o programa deverá ser encerrado,
exibindo o relatório do dia, que conterá a quantidade e o
valor total de prestações pagas no dia. O cálculo do valor a
ser pago é feito da seguinte forma. Para pagamentos sem
atraso, cobrar o valor da prestação. Quando houver atraso,
cobrar 3% de multa, mais 0,1% de juros por dia de atraso.
'''

def valor_pagamento(valor,dias):
    if dias > 0:
        multa = valor * 0.03
        for i in range(dias):
            valor *= 1.001

        return valor+multa
    else:
        return valor

lista = []
juros = 0

while True:
    valor_parcela = float(input('\nQual o valor da parcela (0 para sair)? '))
    if valor_parcela == 0:
        break
    dias_atrasados = int(input('Quantos dias de atraso? '))

    lista.append(valor_pagamento(valor_parcela,dias_atrasados))
    juros += valor_pagamento(valor_parcela,dias_atrasados) - valor_parcela


print(f'\nA quantidade de prestações pagas foram \033[31m{len(lista)}\033[m')
print(f'O valor total pago em prestações foi \033[31mR${sum(lista):.2f}\033[m')
print(f'O valor total pago em juros foi \033[31mR${juros:.2f}\033[m')