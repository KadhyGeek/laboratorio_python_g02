"""Reforzamiento 04"""

"""4. Crear una función y dentro la respectiva excepción para el siguiente
bloque de código para que tu programa no se bloquee y además
imprime un mensaje al usuario la causa y/o solución:
string = "Hello Pythonista"
print(string/0)"""

def cadena():
    # Completa el ejercicio aquí
    try:
        string = "Hello Pythonista"
        print(string/0)
    except TypeError:
        print("ERROR: acceso a cadena incorrecta en Valor ingresado")
    else:
        print("Manejo de cadena correcto")
    finally:
        print("Fin del bloque try")

cadena()

