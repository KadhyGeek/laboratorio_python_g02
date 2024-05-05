"""Reforzamiento 18"""


"""18. Crear una lista con los 15 primeros números impares, luego agregar 3 números flotantes
repetidos (los cuales son impares dentro del rango indicado y que no sea el último
impar).
- Empezando desde 1 y no 0.
- Agregar una cadena en la posición 3 de la lista.
- Eliminar un valor impar de la cadena usando del."""

"""Listas"""

lista = []

for i in range(15):
    lista.append(2*i+1)
    #print(lista[i])

n=1
while n<4:
    lista.append(3.5)
    n+=1
#print(lista)
print("La Lista empezando de la posición 1 y no de 0 es: {}".format(lista[1:len(lista)]))

lista.insert(3, ["SQLServer", "rDS", "MySQL", "postgresql"])

print("La Lista actualizada empezando de la posición 1 y no de 0 es: {}".format(lista[1:len(lista)]))

del lista[5]

print("La última Lista actualizada empezando de la posición 1 y no de 0 es: {}".format(lista[1:len(lista)]))