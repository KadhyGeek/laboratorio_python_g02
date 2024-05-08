"""Reforzamiento 07"""
import lista

"""7. Creando un archivo principal (main.py) donde importará a un módulo
(operaciones.py) el cuál contendrá las siguientes funciones:
- Una función que genere 30 números enteros aleatorios entre 0 y
100, que muestre en pantalla esta lista.
- Otra función que ordene los valores de una lista y volver a
mostrarla."""

from operaciones import listar as ope_1, ordenar as ope_2

lista = ope_1()
print(f"la lista es: {lista}")

lista_ordenada = ope_2(lista)

print(f"la lista es ordenada es: {lista_ordenada}")