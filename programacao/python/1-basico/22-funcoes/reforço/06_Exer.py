
'''
Faça um programa que converta da notação de 24 horas para a
notação de 12 horas. Por exemplo, o programa deve converter
14:25 em 2:25 P.M. A entrada é dada em dois inteiros.

Deve haver pelo menos duas funções: uma para fazer a conversão
e uma para a saída. Registre a informação A.M./P.M. como um
valor ‘A’ para A.M. e ‘P’ para P.M. Assim, a função para
efetuar as conversões terá um parâmetro formal para registrar
se é A.M. ou P.M. Inclua um loop que permita que o usuário
repita esse cálculo para novos valores de entrada todas as
vezes que desejar.
'''


def horario(h,m):
    f = 'AM'
    if h > 12:
        h-=12
        f = 'PM'
    return f'\033[31m{h}:{m} {f}\033[m'


while True:
    hora = int(input('\nDigite a hora? '))
    if hora == 0:
        break
    minuto = int(input('Digite os minutos? '))
    print(horario(hora,minuto))
