from fracao import Fracao
import random as rd


fracoes = []
num = rd.sample(range(3), 3)
den = rd.sample(range(3, 6), 3)

for x in range(len(num)):
    fracoes.append(Fracao(num[x], den[x]))

print(num)
print(den)

nova = rd.sample(fracoes, 1)[0].multiplicar(rd.sample(fracoes, 1)[0])
print(nova.numerador, nova.denominador)


