"""Reforzamiento 09"""

"""9. Crear una función que pida al usuario un número entero entre 1 y 20 y
guarde en un fichero (que no existe) con el nombre tabla.txt la tabla
de multiplicar de ese número, done n es el número introducido."""



import json

json_data = '{"a":1,"b":2,"c":3,"d":4,"e":5}'

json_to_python = json.loads(json_data)
print(json_to_python)

data_python = {'nombre' : "Milagros", 'edad' : 20, 'distrito' : "Jesus Maria", 'promedio' : 16.5}

cata_python_to_json = json.dumps(data_python)
print(cata_python_to_json)



