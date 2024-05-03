"""Reforzamiento 05"""


"""5. Crear una función que aceptará por parámetro dos valores que serán
ingresados por el usuario, una lista donde los valores serán llenados
por el usuario también y un segundo parámetro que eliminará de la
lista que fue ingresada a la función, finalmente el output de la función
será la lista actualizada sin el valor que se sacará de la lista. Mostrar
también la lista original y el número que fue eliminado."""

"""Funciones"""

lista=[]
def agregar_list(a):
    a = int(input("ingresar un valor: "))
    lista.append(a)
    return lista

def eliminar_list(b):
    b = int(input("ingresar que valor desea eliminar: "))
    lista.remove(b)
    return lista

def lista_actuales(lista):
    x=input("marque a para agregar y e para eliminar la lista actuales: ")

lista_actual()
