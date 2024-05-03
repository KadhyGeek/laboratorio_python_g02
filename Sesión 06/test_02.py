"""POO en Python"""
"""Polimorfismo"""


class Perro():
    def sonido(self):
        print("Guaauu")


class Gato():
    def sonido(self):
        print("Miauuu")


class Vaca():
    def sonido(self):
        print("Muuuuu")


gato = Gato()
perro = Perro()
vaca = Vaca()

lista_animales = [perro, gato, vaca]


def canto(animales):
    for animal in animales:
        animal.sonido()


canto(lista_animales)
