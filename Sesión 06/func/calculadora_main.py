from funciones import suma as oper_1, multiplicacion as oper_2

var_1 = int(input("Iingresar un primer valor: "))
var_2 = int(input("Iingresar un segundo valor: "))

sum = oper_1(var_1, var_2)
print("El resultado de sus dos valores es: {}".format(sum))


mul = oper_2(var_1, var_2)
print("El resultado de sus dos valores es: {}".format(mul))
