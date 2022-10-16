from Biblioteca import modulo_exer_108 as md108

valor = int(input('Qual o valor para calcular? '))

print(f'A metade de {md2.formata(valor)} é {md2.metade_real(valor)}')
print(f'O dobro de {md2.formata(valor)} é {md2.dobro_real(valor)}')

taxa1 = int(input('\nQual a taxa de aumento? '))
print(f'Um aumento de {taxa1}% sobre {md2.formata(valor)} fica {md2.aumento_real(valor,taxa1)}')

taxa2 = int(input('\nQual a taxa de subtração? '))
print(f'Um corte de {taxa2}% sobre {md2.formata(valor)} fica {md2.diminuir_real(valor,taxa2)}')








