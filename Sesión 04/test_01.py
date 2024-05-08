"""usando las propiedades de cadenas de string"""

"""Concatenación"""

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
nom_completo = "El nombre completo del usuario es: " + nombre + " " + apellido
print(nom_completo)
nom_completo_2 = f"El nombre completo del usuario es: {nombre} {apellido}"
print(nom_completo_2)
