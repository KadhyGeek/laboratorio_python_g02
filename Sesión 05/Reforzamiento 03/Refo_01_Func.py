"""Reforzamiento 01"""


"""1. Pedir dos números positivos mediante terminal al usuario. Mostrar
como salida el número cuya sumatoria de dígitos es el mayor y los
números cuya sumatoria de dígitos es menor que 10. Utilizar una o
más funciones, según sea conveniente."""

"""Funciones"""



    var_1 = int(input("ingrese un primer número positivo : "))

    var_2 = int(input("ingrese un segundo número positivo : "))


    print( comparar_suma_de_digitos(var_1, var_2) , calcula_menor_que_10(var_1) , calcula_menor_que_10(var_2) )



def comparar_suma_de_digitos(x, y):

    suma_x = suma_de_digitos(x)
    suma_y = suma_de_digitos(y)
    men_x = calcula_menor_que_10(x)
    men_y = calcula_menor_que_10(y)

    return


    tabla={}

    tabla[x] = suma_x
    tabla[y] = suma_y

    if suma_de_digitos(x) > suma_de_digitos(y):
        return f"el numero con mayor suma de digitos es {x}"
    elif suma_de_digitos(y) > suma_de_digitos(x):
        return f"el numero con mayor suma de digitos es {y}"
    else:
        return "La suma de ambos números son iguales", max(suma_x, suma_y)






def calcula_menor_que_10(n):
    if suma_de_digitos(n) < 10:
        return f"La suma de digitos de {n} es menor que 10"




def suma_de_digitos(a):
    a=str(a)
    suma_a=0
    for i in a:
        suma_a+=int(i)
    return suma_a

comparar_suma_de_digitos()
