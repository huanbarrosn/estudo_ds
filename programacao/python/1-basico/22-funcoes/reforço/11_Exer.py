'''
Data com mês por extenso.
Construa uma função que receba uma data no formato DD/MM/AAAA e devolva uma string
no formato D de mesPorExtenso de AAAA. Opcionalmente, valide a data e retorne NULL caso a data seja inválida.
'''


def conversor_data(data):
    meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho',
             'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']

    a = data.split('/')
    b = ''.join(a)

    dia = a[0]
    mes = meses[int(a[1])-1]
    ano = a[2]

    if not len(data) == 10:
        return 'Erro1'

    if not b.isdigit():
        return 'Erro2'

    if not data.find('/') + data.rfind('/') == 7:
        return 'Erro3'


    return f'{int(dia)} de {mes} de {ano}'


print(conversor_data('20/01/2000'))
