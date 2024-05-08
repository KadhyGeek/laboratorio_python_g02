"""Manejo de archivos"""

tecnologias_backend = ["\nPython", "Java", "Node JS", "Ruby"]
tecnologias_frontend = ["\nAngular", "React JS", "Javascript", "Boostrap"]
base_datos = ["\nMysql", "Postgresql", "DYNAMODb"]

"""
    a+: Permite escribir varias líneas en nuestro archivo
    a+: Escribe nuevas líneas de texto sin sobreeescribir el contenido del archivo
"""
file = open("my_files/file_2.txt", "a+")

#file.writelines(tecnologias_backend)
#file.writelines(tecnologias_frontend)
file.writelines(base_datos)

file = open("my_files/file_2.txt", "r")
print(file.read())

"""Cierre del archivo"""
file.close()
