"""Reforzamiento 19"""


"""19. Crea una lista vacía que tendrá 10 valores enteros, pedir al usuario que ingrese cada
uno de sus valores y que finalmente se muestre la suma y la media de los números
ingresados a la lista."""

"""Listas"""

lista = []

for i in range(10):
    lista.append(int(input("Ingrese un número: ")))

print(lista)

print(F"La suma de los elementos escritos es {sum(lista)} y la media de los elementos escritos es {sum(lista)/10}")