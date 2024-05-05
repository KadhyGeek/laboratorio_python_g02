"""Reforzamiento 04"""


"""4. Elimina el key edad tipo de tu diccionario, incluyendo su valor.

del var[‘key’]"""

"""Diccionario"""

empleado = {"nombre": "Margaret", "edad": 27, "salario": 2800, "dni": 24369837}

del empleado["edad"]

print("El diccionario tiene el siguiente contenido: {}".format(empleado))