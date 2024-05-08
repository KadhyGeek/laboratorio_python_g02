import json

"""Uso de la librería JSON"""

data_python = {'nombre': "Milagros", 'edad': 20, 'distrito': "Jesús María", 'promedio': 16.5}

"""Convirtiendo a un dato tipo Json: dumps()"""

data_python_to_json = json.dumps(data_python)

print("Nuestra variable contiene el siguiente dato: {}".format(data_python_to_json))
print(type(data_python_to_json))
