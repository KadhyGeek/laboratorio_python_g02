"""Reforzamiento 03"""


"""3. Crear una función y dentro la respectiva excepción para el siguiente
bloque de código para que tu programa no se bloquee y además
imprime un mensaje al usuario la causa y/o solución:
persona= { 'nombre':'Xavier', 'apellido':'Rodriguez', 'dni':'63325345'}
persona['profesion']"""

def diccionario():
    # Completa el ejercicio aquí
    try:
        persona= { "nombre":"Xavier", "apellido":"Rodriguez", "dni":"63325345"}
        persona["profesion"]
    except KeyError:
        print("ERROR: acceso a clave incorrecta en diccionario")
    else:
        print("Manejo de diccionario correcto")
    finally:
        print("Fin del bloque try")

diccionario()