"""Reforzamiento 02"""


"""2. Convierte tu diccionario a una lista y mostrar el tipo de datos final convertido en consola."""

"""Diccionario"""

empleado = {"nombre": "Margaret", "edad": 27, "salario": 2800}

empleado_values = list(empleado.values())

for i in empleado_values:
    print("Elemento de empleado_values {} y su tipo: ".format(i),type(i))