class Automovel:

    def __init__(self, modelo, cor, velocidade_max):
        self.modelo = modelo
        self.cor = cor
        self.velocidade_max = velocidade_max
        self.velocidade = 0
        self.desacelera = False

    def imprimi(self):
        if self.velocidade == 0:
            print('O automovel está parado')
        elif self.desacelera:
            print(f'O automovel desacelerou {self.desacelera} km/h e sua velocidade atual é {self.velocidade} km/h')
        elif self.velocidade < self.velocidade_max:
            print(f'O automovel está a uma velicidade de {self.velocidade} km/h')
        else:
            print(f'O automovel atingiu sua velocidade maxima de {self.velocidade_max} km/h')

    def acelerar(self, valor_velocidade):
        self.desacelera = False
        self.velocidade = valor_velocidade
        if valor_velocidade >= self.velocidade_max:
            self.velocidade = self.velocidade_max
        self.imprimi()

    def freiar(self, valor_desacelera):
        self.desacelera = valor_desacelera
        self.velocidade -= valor_desacelera
        if self.velocidade < 0:
            self.velocidade = 0
        self.imprimi()

    def parar(self):
        self.velocidade = 0
        self.imprimi()



