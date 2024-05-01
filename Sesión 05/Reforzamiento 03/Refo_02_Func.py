"""Reforzamiento 02"""
import math

"""2. Crea una función que al ingresar dos números por parámetro mostrará
todos los cuadrados de los números que hay entre ellos (Usar la
función una vez y mostrar el resultado por consola). Los números
serán ingresados y solicitados al usuario."""

"""Funciones"""

var_1 = int(input("ingrese un primer número positivo : "))

var_2 = int(input("ingrese un segundo número positivo : "))

def cuadrados_entre(a, b):
    cuadrados = []

    for i in range(a,b + 1):
        n = 1
        while n * n <= i:
            if n*n == i:
                cuadrados.append(i)
            n += 1
    return cuadrados

print(cuadrados_entre(var_1, var_2))
