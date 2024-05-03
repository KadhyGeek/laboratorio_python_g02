"""Gestión de exepciones"""

"""
    Crear una función aplicando exepciones donde no se pueda
    realizar una suma de diferentes tipos de datos
"""


def operaciones(a, b):
    try:
        resultado = a/b
    except TypeError:
        print("No se puede sumar un string con un dato int")
    except ZeroDivisionError:
        print("No se puede dividir entre cero")
        resultado = 0
        print("Resultado: {}".format(resultado))
    else:
        print(resultado)


#operaciones(40, "¡¡Hello Python!!")
#operaciones(100, 500)
operaciones(500, 0)

