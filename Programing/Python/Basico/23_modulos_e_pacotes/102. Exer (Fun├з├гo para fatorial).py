

'''

Exercício Python 102: Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que
indique o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado
ou não na tela o processo de cálculo do fatorial.

'''


def fatorial(numero,mostrar=False):
    """
    :param f: número a retirar o fatorial
    :param show: (opcional) mostra ou ñ o calculo
    :return: printa o fatorial
    """

    a = numero
    b = numero

    while a >= 1:
        # mostrar o calculo
        if mostrar:
            print(a,end='')
            if a > 1:
                print(' x ',end='')
            else:
                print(end=' = ')

        # calcula o fatorial
        a -= 1
        if a == 0:
            break
        b = b*a

    # mostra o resultado do fatorial
    print(b)


num = int(input('Você quer saber o fatorial de qual número? '))
print('*'*48)
fatorial(num,True)
fatorial(num)
print()
help(fatorial)