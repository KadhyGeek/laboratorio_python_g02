"""Manejo de archivos"""

tecnologias_backend = ["\nPython", "\nJava", "\nNode JS", "\nRuby"]

file = open("../Sesión 07/my_files/file_4.txt", "a+")

file.writelines(tecnologias_backend)

file = open("../Sesión 07/my_files/file_4.txt", "r")

tecnologia = input("Iingrese la tecnología a buscar")

for newLine in file:
    #print(newLine)
    if tecnologia in newLine:
        print("Tiene en tu lista a {}".format(tecnologia))

"""Cierre del archivo"""
file.close()

