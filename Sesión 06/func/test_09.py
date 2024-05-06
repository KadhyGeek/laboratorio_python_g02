"""Uso de módulos"""
"""
    1. Crear un módulo donse se va a obtener el impuesto que
    va a pagar una persona si su sueldo es mayor a 5000 soles
    2. Ingresar el nombre y suelos por consola
    3. Crear en el módulo una función que devolverá un mensaje
    indicando "Hola, 'nombre'"
    4. También mostrar un mensaje diciendo "El impuesto que tiene
    que pagar es de 'impuesto'"
    impuesto: 10%  del sueldo
"""

class Cuenta:

    def __init__(self):
        self.titular = input("ingrese nombre del titular: ")
        self.sueldo = int(input("ingrese sueldo del titular: "))

    def Impuesto(self):
        if self.sueldo > 5000:
            print(f"Hola {self.titular}, su sueldo es {self.sueldo}, por lo tanto tiene que pagar un impuesto de {self.sueldo*0.1}")
        else:
            print(f"Hola {self.titular}, su sueldo es {self.sueldo}, no tienes impuestos por pagar")


cuenta_p = Cuenta()

print(cuenta_p.Impuesto())