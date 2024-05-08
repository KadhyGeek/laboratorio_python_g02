"""Uuso de la lobrería JSON para tratar tipos de datos JSON"""

import json

"""Uso de la librería JSON"""
json_data = '{"nombre": "Python", "tipo": "Backend", "paradigma": "POO"}'

"""Convitiendo a un dato manejable para Python"""

json_to_python = json.loads(json_data)

print("Nuestro dato tipo JSON a dato para Python es: {}".format(json_to_python))
print(type(json_to_python))
