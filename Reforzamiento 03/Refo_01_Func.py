"""Reforzamiento 01"""


"""1. Pedir dos números positivos mediante terminal al usuario. Mostrar
como salida el número cuya sumatoria de dígitos es el mayor y los
números cuya sumatoria de dígitos es menor que 10. Utilizar una o
más funciones, según sea conveniente."""

"""Funciones"""

num_1 = int(input("ingrese un primer número positivo : "))
num_2 = int(input("ingrese un segundo número positivo : "))


def comparar_suma_de_digitos(x, y):

    suma_x = suma_de_digitos(x)
    suma_y = suma_de_digitos(y)
    calcula_menor_que_10(x,y)

    tabla={}

    tabla[x] = suma_x
    tabla[y] = suma_y

    if suma_de_digitos(x) > suma_de_digitos(y):
        return f"el numero con mayor suma de digitos es {x} y {calcula_menor_que_10(x,y)}"
    elif suma_de_digitos(y) > suma_de_digitos(x):
        return f"el numero con mayor suma de digitos es {y} y {calcula_menor_que_10(x,y)}"
    else:
        return f"La suma de ambos números son iguales {max(suma_x, suma_y)} y {calcula_menor_que_10(x,y)}"


def calcula_menor_que_10(n,m):
    if suma_de_digitos(n) < 10 < suma_de_digitos(m):
        return f"La suma de digitos de {n} es menor que 10"
    if suma_de_digitos(m) < 10 < suma_de_digitos(n):
        return f"La suma de digitos de {m} es menor que 10"
    if suma_de_digitos(n) < suma_de_digitos(m) < 10 or suma_de_digitos(n) < suma_de_digitos(m) < 10:
        return f"La suma de digitos de {n} y {m} es menor que 10"
    else:
        return f"La suma de digitos de {n} y {m} es mayor que 10"

def suma_de_digitos(a):
    a=str(a)
    suma_a=0
    for i in a:
        suma_a+=int(i)
    return suma_a

compara = comparar_suma_de_digitos(num_1,num_2)
print(compara)
