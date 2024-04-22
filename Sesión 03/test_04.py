"""
Requisitos:
- Dentro de una empresa se va a solicitar pedir nombre
y apellido del empleado.
- Distrito de residencia
- Sueldo y el calculo del bono final del año, que será el
triple de sueldo mensual menos el 10 por ciento del sueldo
- Todo estos datos van a estar asigandos en una lista.
- Por asignación múltiple de variables, asignar los valores
de esta lista a 3 nueva variables.
- Mostrar por la terminal el mensaje de:
"'Nombre' 'apellido' recibirá 'bono' soles de bono de fin de año.
"""

datos=[input("ingresa nombre: "), input("ingresa apellido: "), input("ingresa distrito: "), int(input("ingresa sueldo: "))]

nombre, apellido, distrito, sueldo = datos


bono = (3 * sueldo) - (0.1 * sueldo)

lista=[]

lista.append(nombre)
lista.append(apellido)
lista.append(distrito)
lista.append(sueldo)
lista.append(bono)


print("la lista es: {} ".format(lista))