# https://pokeapi.co/api/v2/pokemon/charizard

# 200: OK
# 404: Error de permisos
# 500: Error de conexión con el servidor

#Instalación: pip install requests

import requests as rq

# https://pokeapi.co/

res = rq.get("https://pokeapi.co/api/v2/pokemon/charizard")

# print("Status code: {}".format(res.status_code))

# json = res.json()
# print("JSON del API: {}".format(json))

json = res.json()

print("Nombre de pokemon dentro del JSON: {}".format(json['forms'][0]['name']))

json['forms'][0]['name'] = "New"
print(json['forms'][0]['name'])


"""Para darle un formato correcto a tus datos en JSON usar: 

https://jsonformatter.curiousconcept.com/#

"""