"""Reforzamiento 14"""


"""14. Crear un módulo y un archivo principal (donde llamará las funciones del
módulo) el módulo tendrá una función para ingresar nombres y
apellidos, una función para pedir el tipo de seguro que tiene y otra
función para indicar si es mayor de edad o no (pedir la edad desde
consola)"""

"""Funciones"""


def registrar():
    nomb = input("Ingrese el nombre: ")
    ape = input("Ingrese el apellido: ")
    ed = int(input("Ingrese la edad: "))
    tipo = pedir(nomb, ape)
    mayor = mayor_edad(ed)
    return f"Hola {nomb} {ape}, por la edad que tienes {ed} año(s) eres {mayor} y tu tipo de seguro es {tipo}"

def pedir(a, b):
    tseguro = input("Ingrese el tipo de seguro: ")
    return tseguro



def mayor_edad(r):
    if r > 18:
        return "mayor de edad"
    else:
        return "menor de edad"


print(registrar())