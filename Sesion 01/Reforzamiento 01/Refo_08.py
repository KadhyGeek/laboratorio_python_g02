"""Tipos de datos"""

"""8.Usando la condicional if imprimir por pantalla si una lista está vacía o no, probar con
una lista vacía y otra con una lista vacía."""



"""Creando variables"""

lista_1 = []
lista_2 = ["perro", "gato", "pato", "loro"]

if len(lista_2) == 0:
    print("Lista esta vacía")
else:
    print("Lista tiene {} elementos".format(len(lista_2)))