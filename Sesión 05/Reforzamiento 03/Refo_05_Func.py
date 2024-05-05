"""Reforzamiento 05"""


"""5. Crear una función que aceptará por parámetro dos valores que serán
ingresados por el usuario, una lista donde los valores serán llenados
por el usuario también y un segundo parámetro que eliminará de la
lista que fue ingresada a la función, finalmente el output de la función
será la lista actualizada sin el valor que se sacará de la lista. Mostrar
también la lista original y el número que fue eliminado."""

"""Funciones"""

lista=[]
def agregar_list(n):
    lista.append(n)
    return lista

def eliminar_list(b):
    lista.remove(b)
    return lista

def lista_actuales(lista):
    print(f"la lista actual contiene {lista}")
    opcion=input("marque 'a' para agregar y 'e' para eliminar un elemento de la lista la lista actuales: ")
    if opcion=="a":
        elemento = input("escriba que elemento quiere agregar a la lista: ")
        print("Despues de agregar su elemento, la lista actual es: ", agregar_list(elemento), lista_actuales(lista))
    elif opcion=="e":
        elemento = input("escriba que elemento de la lista que quiere eliminar a la lista: ")
        print("Despues de eliminar su elemento, la lista actual es: ", eliminar_list(elemento), lista_actuales(lista))
    else:
        exit()
    return lista
lista_actuales(lista)
