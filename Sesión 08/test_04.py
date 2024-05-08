"""Manejo de archivos"""

"""Apertura y lectura de archivo"""
"""
    r: Abre el archivo en modo lectura
"""

file = open("my_files/file.txt", "r")

"""
    read(): Nos permite leer el contenido de un archivo
"""

print("El contenido de nuestro archivo 'file': {}".format(file.read()))

"""Cierre de archivo"""
file.close()
