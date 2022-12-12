from fracao import Fracao
import random as rd


f1 = Fracao(1, 2)

fracoes = [Fracao(rd.randint(1, 10), rd.randint(1, 10)) for x in range(10)]

f2 = f1.encontrar_equivalente(fracoes)


for fracao in f2:
    print(fracao.numerador, fracao.denominador, end="\n")
