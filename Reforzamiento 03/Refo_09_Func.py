"""Reforzamiento 09"""
import math

"""9. Crear una clase llamada círculo que contenga radio en su constructory
que contenga un método área que devuelva el área de un círculo.
Aplicar excepciones en caso no se ingrese un dato tipo numérico.
Crear adicionalmente un método que devuelva el perímetro del círculo.
Instanciar la clase respectivamente para dos diferentes radios.
Habrá un método donde pedirá el radio del círculo.
Instanciar mínimo 2 veces la clase y mostrar resultados por consola."""

"""Funciones"""

class Circulo:
    def __int__(self):
            try:
                self.rad = int(input("Ingrese el radio del circulo: "))

            except ValueError:
                print("Por favor ingrese un valor numérico")
                exit()
    def area(self):
        self.areac = math.pi * (self.rad ** 2)
        return self.areac

    def perimetro(self):
        self.peric = 2 * math.pi * self.rad
        return self.peric


                



dat_circ = Circulo()

print(dat_circ.__int__())
print(dat_circ.area())
print(dat_circ.perimetro())



