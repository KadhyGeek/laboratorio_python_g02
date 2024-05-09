"""Reforzamiento 12"""

"""12. Crear una función decoradora que dará los buenos días antes de
ejecutar una función a ser decorada y luego de ser ejecutada lanzará
un mensaje diciendo “Hasta luego”.
La función a decorar pedirá el nombre de una persona y retornará el
mensaje “Soy ‘nombre’”."""

def saludar(funcion_parametro):
    def saludo():
        print("Buenos días")
        funcion_parametro()
        print("Hasta Luego")
    return saludo()


@saludar
def saludo():
    nombre = input("Ingrese el nombre del persona que desea saludar: ")
    print("Soy "+nombre)









