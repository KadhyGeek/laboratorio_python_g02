"""Reforzamiento 01"""

"""1. Crear una función para encontrar el error en el siguiente bloque de
código. Crea una excepción para evitar que tu programa se bloquee y
además imprime un mensaje al usuario la causa y/o solución:
suma = 80 + “Hola Pythonista”"""

def sum():
# Completa el ejercicio aquí
    try:
        suma = 80 + "Pythonista"
    except TypeError:
        print("ERROR: intento de suma de número y cadena")
    else:
        print("Operación realizada correctamente")
    finally:
        print("Fin del bloque try")

print(sum())






