from Biblioteca import modulo_exer_109 as md109

valor = int(input('Qual o valor para calcular? '))
valor_ofc = md3.formata(valor)

print(f'A metade de {valor_ofc} é {md3.metade_real(valor)}')
print(f'O dobro de {valor_ofc} é {md3.dobro_real(valor)}')

taxa1 = int(input('\nQual a taxa de aumento? '))
valor_aumento = md3.aumento_real(valor,taxa1)
print(f'Um aumento de {taxa1}% sobre {valor_ofc} fica {valor_aumento}')

taxa2 = int(input('\nQual a taxa de subtração? '))
valor_diminuir = md3.diminuir_real(valor,taxa2)
print(f'Um corte de {taxa2}% sobre {valor_ofc} fica {valor_diminuir}')

