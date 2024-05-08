"""Usando las propiedades de cadenas o string"""
"""
Requisitos:
- Ingresar tu nombre y apellido por consola (cada valor tiene que
estar en una variable disintinta)
- Concatener ambos valores en una sola variable
- Obtener y mostrar el tamaño del nombre completo
- Imprimir el resultado final todo en mayúsculas
- Indicar mediante condicionales si el tamaño del nombre es
mayor o no al del apellido (ingresar solo para este caso el
apellido paterno)
"""
nombre = input("Ingrese el nombre del usuario: ")

apellido = input("Ingrese el apellido del usuario: ")

nom_compl = nombre+" "+apellido
maynom = nom_compl.upper()
caract = len(nom_compl)

print(f"El nombre completo del usuario es: {maynom} y su tamaño de: {caract}")

if len(nombre) > len(apellido):

    print("El nombre es mas largo que el apellido")
else:
    print("El nombre es menor que el apellido")
