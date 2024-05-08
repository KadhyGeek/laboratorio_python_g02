"""Reforzamiento 06"""

"""6. Creando un archivo principal donde llamará a un módulo
(operaciones.py) el cuál contendrá las siguientes funciones.
- La primera función cargará una un número entero que pedirá al
usuario que ingrese por consola un valor.
- La segunda función solamente sumará dos valores.
- Desde el archivo principal importar al módulo y sumar dos valores
usando las funciones anteriormente creadas en el módulo"""

from operaciones import valor as oper_1, valor as oper_2 , suma as oper_3

num_1 = oper_1()
num_2 = oper_2()

sum = oper_3(num_1, num_2)

print(f"el primer numero indicado es {num_1}, el segundo numero es {num_2} y la suma de ambos es {sum}")


