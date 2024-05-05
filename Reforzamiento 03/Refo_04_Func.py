"""Reforzamiento 04"""


"""4. Pedir al usuario que ingrese una oración con un mínimo de 3 palabras
la cual será usada por parámetro para una función que se creará e
indicará cuantas palabras existen dentro de la oración ingresada."""

"""Funciones"""

oracion = input("Ingrese una opración que tenga mas de 3 palabras: ")

def numero_de_palabras(oracion):
    palabras = oracion.split()
    cantidad_de_palabras = len(palabras)
    return cantidad_de_palabras

resulta = numero_de_palabras(oracion)

print(f"La oracion ingresada contiene {resulta} palabras")