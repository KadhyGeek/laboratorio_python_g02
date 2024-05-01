"""Reforzamiento 01"""


"""1. Pedir dos números positivos mediante terminal al usuario. Mostrar
como salida el número cuya sumatoria de dígitos es el mayor y los
números cuya sumatoria de dígitos es menor que 10. Utilizar una o
más funciones, según sea conveniente."""

"""Funciones"""

var_1 = int(input("ingrese un primer número positivo : "))

var_2 = int(input("ingrese un segundo número positivo : "))


def comparar_suma_de_digitos(x, y):

    suma_x = suma_de_digitos(x)
    suma_y = suma_de_digitos(y)

    tabla={}

    tabla[x] = suma_x
    tabla[y] = suma_y

    if suma_de_digitos(x) > suma_de_digitos(y):
        return x
    elif suma_de_digitos(y) > suma_de_digitos(x):
        return y
    else:
        return "La suma de ambos números son iguales", max(suma_x, suma_y)

q


def suma_de_digitos(a):
    a=str(a)
    suma_a=0
    for i in a:
        suma_a+=int(i)
    return suma_a


print(comparar_suma_de_digitos(var_1,var_2))