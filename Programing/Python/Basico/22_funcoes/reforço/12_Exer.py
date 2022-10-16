'''
Embaralha palavra.
Construa uma função que receba uma string como parâmetro e devolva outra string com os carateres embaralhados.
Por exemplo: se função receber a palavra python, pode retornar npthyo, ophtyn ou
qualquer outra combinação possível, de forma aleatória. Padronize em sua função que todos os caracteres serão
devolvidos em caixa alta ou caixa baixa, independentemente de como foram digitados.
'''


from random import *

# receber um dado em str
def embaralhar(palavra,f=0):

    # caixa alta ou baixa
    if f == 1:
        palavra = palavra.casefold()
    if f == 2:
        palavra = palavra.upper()

    # embaralhar a palavra
    plv_embaralhada = sample(palavra, len(palavra))

    # printar a palavra
    print(''.join(plv_embaralhada))



embaralhar('Abacate')



