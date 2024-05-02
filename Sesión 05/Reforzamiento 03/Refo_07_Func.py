"""Reforzamiento 07"""


"""7. Crear una clase en python que contenga un método que revierta una
cadena de palabras.
Input: "Hola Pythonista, seguimos adelante"
Output: "adelante seguimos Pythonista Hola"
Llamarlo mínimo 2 veces y mostrar el resultado por consola."""

"""Funciones"""

class Fraseinvertida:
    def invertir_texto(self, texto):
        resultado= ' '.join(reversed(texto.split()))
        return resultado


texto = input("Ingrese un texto : ")

operaciones = Fraseinvertida()

print(operaciones.invertir_texto(texto))

print(Fraseinvertida().invertir_texto(texto))


