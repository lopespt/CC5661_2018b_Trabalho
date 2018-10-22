import numpy as np
import itertools as it
import random


def geraMatriz(n,m):
    x = np.random.uniform(high=100, size=(n,m))
    x = np.round(x,2)
    return x.tolist()


def geraProblema1():
    elementos = np.random.random_integers(0,9999999999999,(np.random.random_integers(100,1000)))
    obj ={
        "tipo": "ordenacao",
        "n": len(elementos),
        "elementos": elementos.tolist()
    }
    return obj

def geraProblema2():

    dimensoes = np.random.random_integers(3,30,(np.random.random_integers(3,5)))
    
    d1, d2 = it.tee(dimensoes)
    next(d2)

    matrizes = []
    for n,m in zip(d1,d2):
        matrizes.append({"linhas": int(n), "colunas": int(m), "matriz": geraMatriz(n,m)})

    obj = {
        "tipo": "multiplicacao_matrizes",
        "n_matrizes": len(dimensoes) -1,
        "matrizes": matrizes
    }

    return obj
    
    

def geraProblema3():
    tam_grafo = np.random.randint(5,15)
    matriz_adjac = np.random.randint(1,20,(tam_grafo,tam_grafo))
    densidade = np.random.uniform(0.7)
    vertices = np.random.permutation(range(0,tam_grafo))

    mat_densi = np.random.random((tam_grafo, tam_grafo)) <= densidade
    #zerar diagonais

    matriz_adjac = matriz_adjac*mat_densi
    tam_grafo = 6
    matriz_adjac = np.zeros( (tam_grafo,tam_grafo))
    matriz_adjac[0,1] = 2
    matriz_adjac[0,4] = 2
    matriz_adjac[1,0] = 2
    matriz_adjac[1,2] = 2
    matriz_adjac[1,4] = 0.2
    matriz_adjac[4,0] = 2
    #matriz_adjac[4,1] = 0.2
    #matriz_adjac[4,3] = 0.1
    matriz_adjac[4,5] = 1
    matriz_adjac[2,1] = 2
    matriz_adjac[2,5] = 1
    matriz_adjac[2,3] = 3
    #matriz_adjac[3,2] = 2
    #matriz_adjac[3,4] = 0.1
    matriz_adjac[3,5] = 1
    matriz_adjac[5,4] = 1
    matriz_adjac[5,2] = 1
    #matriz_adjac[5,3] = 1
   

    vertices = [1,3,5]
    obj = {
        "tipo": "grafo",
        "n_nos": tam_grafo,
        "mat_pesos": matriz_adjac.tolist(),
        "passar_em": vertices[:3]#.tolist()
    }

    return obj
