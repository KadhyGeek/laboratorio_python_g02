"""Reforzamiento 06"""

"""6. Escribir una clase en Python que contenga un método que convierta un
número entero en su cubo y contenga otro método que obtenga el
cuadrado de ese resultado. El valor inicial de resultado deberá estar
creado en el constructor. Considerar un método en la cual le pedirá al
usuario ingresar un valor numérico."""

"""Funciones"""


class Numero:
    def __init__(self):
        self.num = int(input("Ingrese un número: "))

    def cubo(self):
        self.cub = self.num ** 3
        return self.cub

    def cuadrado(self):
        cuadr = self.cub ** 2
        return cuadr


numero = Numero()
print(numero.cubo())
print(numero.cuadrado())
