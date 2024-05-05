"""Reforzamiento 03"""


"""3. Crear una función que sume los dígitos del número ingresado y
muestre por consola la suma de estos dígitos."""

"""Funciones"""

var_1 = int(input("Ingrese por un número: "))
def suma_de_digitos(a):
    a=str(a)
    suma_a=0
    for i in a:
        suma_a+=int(i)
    return suma_a


print(f"La suma de los digitos del numero {var_1} son {suma_de_digitos(var_1)}")

