"""Uso del flujo condicional: 'if'"""
"""if ternario"""

"""
Requisitos:
- Ingresar por teclado el sueldo de un empleado
- Si el sueldo es mayor 3000, imprimir "Su sueldo no 
tiene bonificación"
- Caso contrario: "Su sueldo tiene bonificación este año"
"""

sueldo=int(input("Ingrese su sueldo: "))

mensaje = "Su sueldo no tiene bonificacion" if sueldo > 3000  else "Su sueldo tiene bonificacion este año"

print(mensaje)