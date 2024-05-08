"""Decoradores en Python"""

"""Creación interna de la función decoradora"""


def funcionA(funcionB):

    def funcionC():
        print("1. Antes de ejecutar la función que sido decorada")
        funcionB()
        print("2. Después de ejecutar la función que ha sido decorada")

    return funcionC()

@funcionA
def saludo():
    print("Hola Pythonistas!!!")

#saludo()
