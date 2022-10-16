from pacote_exer_111.moedas import funcoes_moedas as fm

num = int(input('Digite o valor a ser analisado: R$'))
tx_a = int(input('Digite o valor da taxa de aumento: '))
tx_c = int(input('Digite o valor da taxa de corte: '))
print()
fm.resumo(num,tx_a,tx_c)