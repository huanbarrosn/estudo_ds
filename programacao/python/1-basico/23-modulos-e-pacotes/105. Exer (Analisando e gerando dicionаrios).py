
'''

Exercício Python 105: Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar
um dicionário com as seguintes informações:

- Quantidade de notas
- A maior nota
- A menor nota
- A média das notas
- A situação (opcional)

nota < 3 : Reprovado
nota < 7 : Recuperação
nota >= 7 : Aprovado

'''


def notas(*n,situação=False):
    media = sum(n)/len(n)

    dic = {
        'Total de notas': len(n),
        'Maior nota': max(n),
        'Menor nota': min(n),
        'Media notas': media
    }

    if media < 3:
        s = 'Reprovado'
    elif media < 7:
        s = 'Recuperação'
    elif media >= 7:
        s = 'Aprovado'

    if situação:
        dic['Situação'] = s

    return dic



anulo = notas(2,2,2,situação=True)
print(anulo)