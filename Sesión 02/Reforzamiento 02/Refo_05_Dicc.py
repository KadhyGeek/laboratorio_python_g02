"""Reforzamiento 05"""


"""5. Convertir tu diccionario a una lista y mostrar en consola el tipo de datos final que tiene."""

"""Diccionario"""

datos = {"nombre": "Margaret", "salario": 2800, "dni": 24369837}

datos_values = list(datos.values())

for i in datos_values:
    print("Elemento de empleado_values {} y su tipo: ".format(i),type(i))