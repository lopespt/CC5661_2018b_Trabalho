import numpy as np
import itertools as it

def geraMatriz(n,m):
    x = np.random.uniform(high=100, size=(n,m))
    x = np.round(x,2)
    return x.tolist()


def geraProblema1():
    elementos = np.random.random_integers(0,9999999999999,(np.random.random_integers(100,1000)))
    obj ={
        "problema": "ordenacao",
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
        "problema": "multiplicacao_matrizes",
        "n_matrizes": len(dimensoes) -1,
        "matrizes": matrizes
    }

    return obj
    
    

def geraProblema3():
    tam_grafo = np.random.randint(5,15)
    matriz_adjac = np.random.randint(1,20,(tam_grafo,tam_grafo))
    densidade = np.random.uniform(0.2)

    mat_densi = np.random.random((tam_grafo, tam_grafo)) <= densidade

    matriz_adjac = matriz_adjac*mat_densi

    obj = {
        "problema": "grafo",
        "n_nos": tam_grafo,
        "mat_pesos": matriz_adjac.tolist()
    }

    return obj
