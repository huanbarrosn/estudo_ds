def matriz(shape, inicio = None, fim= None):

    import numpy as np
    from random import randint
    
    linha = shape[0]
    coluna = shape[1]
    ordem = linha*coluna
    
    if inicio == None:
        inicio = randint(1, 10000)
        fim = inicio + (ordem-1)
    
    intervalo = [x for x in range(inicio, fim+1)]
    quantidade_elementos = len(intervalo)
    
    if ordem != quantidade_elementos:
        return('Nao e possivel criar uma matriz com essa ordem e quantidade de numeros.')
    
    matriz = []
    lixo = []
    comeco = 0 
    
    for x in range(shape[0]):
        for y in range(comeco, coluna):
            lixo.append(intervalo[y])
        
        matriz.append(lixo[:])
        lixo.clear()
    
        coluna += shape[1]
        comeco += shape[1]
        
        
    #return (np.array(matriz))    
    return matriz[:]