"""Reforzamiento 09"""

"""9. Crear una función que pida al usuario un número entero entre 1 y 20 y
guarde en un fichero (que no existe) con el nombre tabla.txt la tabla
de multiplicar de ese número, done n es el número introducido."""

def multiplicar():
    try:
        num = int(input("Ingrese un número entero del 1 al 20: "))
        file = open("my_file_work/Tabla.txt", "w")
        if 0 < num < 21:
            file.write("\n**************************************************\n")
            file.write("--------------TABLA DE MULTIPLICAR----------------\n")
            file.write("**************************************************\n")
            for i in range(num+1):
                file.write(str(num)+" * "+str(i)+" = "+str(num*i)+"\n")
            file = open("my_file_work/Tabla.txt", "r")
            print(f"Nuestro archivo tabla.txt tiene el sgt contenido: {file.read()}")
            file.close()
        else:
            multiplicar()
    except ValueError:
        multiplicar()



multiplicar()






