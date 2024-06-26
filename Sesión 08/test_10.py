"""Decoradores en Python"""

"""Creación de la función decoradora"""


def funcionA(funcionB):
    def funcionC(*args, **kwargs):
        print("1. Antes de ejecutar la función que sido decorada")
        resultado = funcionB(*args, **kwargs)
        print("2. Después de ejecutar la función que ha sido decorada")
        return resultado
    return funcionC

@funcionA
def saludar(nombre, apellido, edad, **kawargs):
    print("Hola {} {}, usted tiene {} años".format(nombre, apellido, edad))
    for key, value in kawargs.items():
        print("{} = {}".format(key, value))


nombre = input("Ingrese su nombre por favor: ")
apellido = input("Ingrese su apellido por favor: ")
edad = input("Ingrese su edad finalmente: ")

saludar(nombre, apellido, edad, ciudad1="Lima", ciudad2="Tacna", ciudad3="Arequipa")
