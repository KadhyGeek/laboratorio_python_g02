import random


def listar():
    lista = [0] * 30
    for i in range(30):
        lista[i] = random.randint(1, 100)
    return lista


def ordenar(x):
    lis = list(x)
    return sorted(lis)

