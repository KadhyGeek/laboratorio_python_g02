"""

Crear 3 variables: nombre, edad, país de residencia y distrito

requisitos:
- Nombre: string, edad: int, país de residencia: string, distrito: string
- Concatenar estos datos e indicar una oración como la siguiente
José tiene X años, es del distrito de "distrito" y viene de "país de residencia"
- Obtener el módulo de su edad al usarlo con el número 5, mostrar el módulo por consola
"""

var_1 = "André"
var_2 = "26"
var_3 = "San Isidro"
var_4 = "Perú"


print("{} tiene {} años, es del distrito de {} y viene de {}".format(var_1,var_2,var_3, var_4))

modulo= edad % 5

print("El módulo de su edad dibvidido entre 5 es: {}".format(modulo))