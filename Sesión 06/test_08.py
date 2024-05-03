from func import funciones

var_1 = int(input("Ingresar un primer valor: "))
var_2 = int(input("Ingresar un segundo valor: "))

sum = funciones.suma(var_1, var_2)
print("El resultado de sus dos valores es: {}".format(sum))


rest = funciones.resta(var_1, var_2)
print("El resultado de sus dos valores es: {}".format(rest))
