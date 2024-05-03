"""Gestión de expeciones"""

"""Estructura y uso"""
"""
try:
    bloque de código 1
except 'excepcion_1'
    bloque de código 2
else:
    bloque de código 3
"""


def division(a, b):
    try:
        resultado = a/b
    except ZeroDivisionError:
        print("¡No se puede dividir entre cero!")
    else:
        print(resultado)


division(40, 0)
division(190, 5)
