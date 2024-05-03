"""Reforzamiento 13"""


"""13. Crear una clase Persona que contenga dos atributos: nombre y edad.
Nombre y edad se ingresarán por teclado en el constructor.
Declarar una segunda clase llamada Empleado que herede de la clase
Persona y agregue un atributo sueldo y muestre si debe pagar
impuestos (10% de su sueldo) (si sueldo es superior a 4000 soles)
Instanciar la clase Empleado, mostrar el sueldo del empleado y cuánto
debe pagar de impuesto."""

"""Funciones"""

class Persona:
    def __init__(self):
        self.nombre =input("Ingrese el nombre: ")
        self.edad = int(input("Ingrese el edad: "))


class Empleado(Persona):
    def __init__(self, nombre, edad):
        self.sueldo = int(input("Ingrese el sueldo del empleado: "))

    def impuesto(self):
        if self.sueldo > 4000:
            self.impuesto =  self.sueldo * 0.1
            return  f"El sueldo del empleado es: {self.sueldo} y el impuesto a pagar es: {self.impuesto}"
        else:
            return f"El sueldo del empleado es: {self.sueldo} y no tiene impuestos por pagar"

persona = Persona()

empleado = Empleado(persona.nombre, persona.edad)
print(empleado.sueldo)
print(empleado.impuesto())
