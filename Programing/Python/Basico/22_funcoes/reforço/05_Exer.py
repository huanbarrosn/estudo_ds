
'''
Faça um programa com uma função chamada somaImposto.
A função possui dois parâmetros formais: taxaImposto, que
é a quantia de imposto sobre vendas expressa em porcentagem e
custo, que é o custo de um item antes do imposto.

A função “altera” o valor de custo para incluir o imposto
sobre vendas.
'''


def soma_imposto(taxa,custo):
    por = (taxa/100)*custo
    return custo+por

print(soma_imposto(10,100))