"""Programación funcional en Python"""

"""
Requisitos:
- Un usuario ingresará 2 números por consola
- En una función obtener si el segundo número 
ingresado es múltiplo del primo o viceversa
- Retornar quién fue múltiplo de quién
"""

a = int(input("Ingresa un primer número : "))
b = int(input("Ingresa un segundo número : "))

def multiplo(x, y):
    if x % y == 0:
        print(F"{x} es múltiplo de {y}")
    elif y % x == 0:
        print(F"{x} es múltiplo de {y}")
    else:
        print(F"Ni {x} ni {y} son múltiplos entre sí ")

mult = multiplo(a,b)
