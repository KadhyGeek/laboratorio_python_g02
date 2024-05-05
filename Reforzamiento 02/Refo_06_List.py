"""Reforzamiento 06"""


"""6. Devuelve la cantidad de veces que se repite un curso (agregarla previamente a tu lista
para que la respuesta sea mayor de 2) dentro de la lista."""

"""Variables"""

cursos = ["MySQL", "Algoritmos", "Python", "Redes", "Android" ,"PHP", "Java", "Oracle", "SQLServer", "SAP", "Auditoría", "Modelamiento"]

cursos.append("PHP")
cursos.append("PHP")
cursos.append("PHP")
cursos.append("PHP")
cursos.append("Android")
cursos.append("Android")

print("Mi lista actualizada es: {}".format(cursos))
print("La cantidad de veces que se repite 'PHP' es: {}".format(cursos.count("PHP")))
print("La cantidad de veces que se repite 'Android' es: {}".format(cursos.count("Android")))