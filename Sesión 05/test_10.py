"""Programación funcional en Python"""

"""
Requisitos:
- Solicitar al usuario 4 número por consola
-  Crear una función que devuelve cuál es el número mayor de 
los 4 ingresados por el usuario
- Finalmente elevar al cubo resultado y mostrarlo 
por consola
"""


var_1=int(input("ingrese un primer numero : "))
var_2=int(input("ingrese un segundo numero :"))
var_3=int(input("ingrese un tercero numero : "))
var_4=int(input("ingrese un cuarto numero : "))

def mayor_al_cubo(a,b,c,d):
    return pow(max(a,b,c,d),3)

print("El mayor numero es: ",max(var_1,var_2,var_3,var_4))

print("El cubo de numero es: ", mayor_al_cubo(var_1,var_2,var_3,var_4))


