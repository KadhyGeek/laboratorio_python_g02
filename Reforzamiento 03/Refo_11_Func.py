"""Reforzamiento 11"""


"""11. Crear una clase Persona con los siguientes requerimientos.
La clase tendrá como atributos el nombre, edad y sueldo de una
persona. Implementar los métodos necesarios para inicializar los
atributos (constructor), un método para mostrar los datos e indicar si
la persona es mayor de edad o no y otro método que bonificación que
retornará el 20% adicional de su sueldo.
Instanciar por lo menos la clase con 2 diferentes personas."""

"""Funciones"""

class Persona:
    def __init__(self, nombre, edad, sueldo):
        self.nombre = nombre
        self.edad = edad
        self.sueldo = sueldo

    def mostrar_datos(self):
        return f"Hola {self.nombre},por la edad que tiene {self.edad}, usted es {self.mayor_edad()}, su sueldo es {self.sueldo} y {self.bonificacion()}"

    def mayor_edad(self):
        if self.edad < 18:
            return "menor de edad"
        else:
            return "mayor de edad"

    def bonificacion(self):
        if self.mayor_edad() == "mayor de edad":
            return f"recibirá {self.sueldo*0.2} e bonificación"
        else:
            return "no recibirá bonificación"


persona_1 = Persona("Pablo", 18, 5000)
print(persona_1.mostrar_datos())
persona_2 = Persona("Rosa", 16, 1000)
print(persona_2.mostrar_datos())