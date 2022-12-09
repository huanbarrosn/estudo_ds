class Fracao:
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador

    def inverter(self):
        return Fracao(self.denominador, self.numerador)

    def negar(self):
        return Fracao(-self.numerador, self.denominador)

    def somar(self, *fracao):

        # Usarei a função soma dentro da função subtrair pois quase 100% do calculo seria o mesmo
        # A condição serve para definir se será soma ou subtração de frações
        sinal = '+'
        if type(fracao[0]) == tuple:
            fracao = fracao[0]
            sinal = '-'

        # Somando frações com denominadores iguais
        num = 0
        teste = True

        for d in fracao:
            if self.denominador != d.denominador:
                teste = False
                break

            num += d.numerador

        if teste:
            return Fracao(self.numerador+num, self.denominador)

        # Somando frações com denominadores diferentes
        # Encontrando o MMC que será o denominador da fração
        denominadores = [self.denominador] + [d.denominador for d in fracao]
        multiplos = []
        n = 2

        while True:
            lista = []
            k = False

            for d in denominadores:
                if d % n == 0:
                    k = True
                    lista.append(d/n)
                else:
                    lista.append(d)

            if k:
                multiplos.append(n)
            else:
                n += 1

            denominadores = lista[:]

            if sum(denominadores) == len(denominadores):
                break

            lista.clear()

        mmc = multiplos[0]
        for n in multiplos[1:]:
            mmc = mmc * n

        # Encontrando o numerador da fração
        num = 0
        fracao = [self]+list(fracao)

        if sinal == '-':
            num = mmc/fracao[0].denominador*fracao[0].numerador
            for n in fracao[1:]:
                num = num - (mmc/n.denominador*n.numerador)

        if sinal == '+':
            for d in fracao:
                print('aqui')
                num += ((mmc/d.denominador)*d.numerador)

        # Retornando a nova fração
        return Fracao(float(num), float(mmc))

    def subtrair(self, *fracao_sub):
        return self.somar(fracao_sub)

    def multiplicar(self, *fracao_mul):
        # Altera o valor de fração na hora da divisão (só é ultilizado quando o metodo dividir é chamado)
        if type(fracao_mul[0]) == tuple:
            fracao_mul = fracao_mul[0]

        # Calculando o coeficiente de n frações (n>2)
        if len(fracao_mul) > 1:
            # Numerador
            num = fracao_mul[0].numerador
            for n in fracao_mul[1:]:
                num = num * n.numerador

            # Denominador
            den = fracao_mul[0].denominador
            for d in fracao_mul[1:]:
                den = den * d.denominador

            # Retorno1
            return Fracao(self.numerador*num, self.denominador*den)

        # Calculando o multiplicação de 2 fração
        else:
            # Retorno2
            f = fracao_mul[0]
            return Fracao(self.numerador*f.numerador, self.denominador*f.denominador)

    def dividir(self, *fracao_div):
        x = self.inverter()
        x = x.multiplicar(fracao_div)
        return x.inverter()

    def equivalente(self, fracao_equi):
        if fracao_equi.numerador/fracao_equi.denominador == self.numerador/self.denominador:
            return True
        else:
            return False

    def encontrar_equivalente(self, fracoes:list):
        f_equivalentes = []
        
        for f in fracoes:
            if f.numerador/f.denominador == self.numerador/self.denominador:
                f_equivalentes.append(f)

        return f_equivalentes


# Testando os métodos
if __name__ == '__main__':

    # Metodo .quivalente()
    a = Fracao(12, 30)
    b = Fracao(2, 5)
    c = Fracao(2, 3)
