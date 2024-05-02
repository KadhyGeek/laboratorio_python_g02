"""Reforzamiento 08"""


"""8. Crear una clase que contenga dos métodos, uno que pida ingresar un
nombre y apellido, un método para pedir su edad y otro método que lo
imprima ambos resultados, pero estarán contenidos en un diccionario.
Comprobar ambos métodos instanciado la clase respectivamente.
Considerar en el constructor los valores necesarios."""

"""Funciones"""


class Persona:
    def __init__(self):
        self.dicc_persona = {}

    def agregre_nom_y_ape(self):
        self.dicc_persona["nombre"] = input("ingrese el nombre de la persona: ")
        self.dicc_persona["apellido"] = input("ingrese el apellido de la persona: ")


    def agregue_edad(self):
        self.dicc_persona["edad"] = str(int(input("ingrese la edad de la persona: ")))
        return self.dicc_persona




datpersona = Persona()


print(datpersona.agregue_edad())

