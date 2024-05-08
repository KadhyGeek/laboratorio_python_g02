"""Usando las propiedades de cadenas o string"""

"""Replace"""
cadena = "Conexión a Base de Datos con Python"
cadena_2 = cadena.replace(cadena[0:6], "pppppppp")
print(f"Cadena con reemplazo, tiene el sgt valor actualizado: {cadena_2}")
"""Eliminación de espacion en blaco de mi cadena (después)"""
cadena_3 = "Conexión a Base de Datos con Python           "
cadena_4 = cadena_3.rstrip()
print(cadena_3)
print(f"Mi cadena actualizada sin espacios en blanco es: {cadena_4}")
