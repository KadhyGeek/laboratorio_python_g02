
"""Listas en  Python"""

"""Requisitos:

- Crear dos listas vacías inicialmente
- Agregar luego los datos de nombre, edad y profesión para ambos (usando append)
- Sumar ambas listas y mostrar el resultado en consola
- Mostrar de manera inversa la suma de ambas listas
- Actualizar la nueva lista eliminando las edad de ambas personas con remove
"""

#Creamos nuestras variables iniciales
var_1 = []
var_2 = []

#Agregamos los datos solicitados para ambas listas

#Sumamos ambas listas

#

var_1.append("Alicia")
var_1.append(25)
var_1.append("Contadora")
var_2.append("Rodrigo")
var_2.append(22)
var_2.append("Programador")

print("La lista 1 es: {}".format(var_1)),
print("La lista 2 es: {}".format(var_2))

sum = var_1 + var_2

print("La lista suma de las listas es: {}".format(sum))

var_1.reverse()
var_2.reverse()

var_1.remove(25)
var_2.remove(22)
print("La lista 1 es: {}".format(var_1)),
print("La lista 2 es: {}".format(var_2))
