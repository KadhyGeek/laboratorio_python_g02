"""Reforzamiento 02"""

"""Crear una función y dentro la respectiva excepción para el siguiente
bloque de código para que tu programa no se bloquee y además
imprime un mensaje al usuario la causa y/o solución:
lista = [2, 6, 10, 4, 5, 23, 1]
lista[10]"""

def lista():
    # Completa el ejercicio aquí
    try:
        lista = [2, 6, 10, 4, 5, 23, 1]
        lista[10]
        #lista[2]=24
    except IndexError:
        print("ERROR: acceso a índice incorrecto en lista")
    else:
        print("Manejo de listas correcto")
    finally:
        print("Fin del bloque try")

lista()

