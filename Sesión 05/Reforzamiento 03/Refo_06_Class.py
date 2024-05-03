"""Reforzamiento 06"""

"""6. Escribir una clase en Python que contenga un método que convierta un
número entero en su cubo y contenga otro método que obtenga el
cuadrado de ese resultado. El valor inicial de resultado deberá estar
creado en el constructor. Considerar un método en la cual le pedirá al
usuario ingresar un valor numérico."""

"""Funciones"""


class Numero:
    def __init__(self):
        self.num = self.valor()

    def cub_num(self):
        self.c = self.num ** 3
        return self.c
    def valor(self):
        self.num = int(input("ingrese un numero: "))

    def cua_cub(self):
        self.cub_num()
        self.cuacub = pow(self.cub, 2)
        return self.cuacub


num = Numero()
#print(num.cub_num())
print(num.cua_cub())
print(num.valor())