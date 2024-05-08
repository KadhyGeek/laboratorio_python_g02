"""Reforzamiento 08"""

"""8. Creando un archivo principal (main.py) donde importará a un módulo
(operaciones.py) el cuál contendrá las siguientes funciones:

- Una función que realizará la carga de un valor entero.
- Una función que mostrará por pantalla la raíz cuadrada de dicho
valor
- Y otra función el valor elevado al cuadrado y al cubo de dicho
número.
- Utilizar el módulo math de python."""

from operaciones import valor as oper_1, raiz as oper_2 , cua_cub as oper_3

num = oper_1()

raiz_c = oper_2(num)

print(f"la raiz cuadrada del numero {num} es {raiz_c}")

cuadr, cubo = oper_3(num)

print(f"el cuadrado del numero {num} es {cuadr} y el cubo es {cubo}")





