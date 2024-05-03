"""Uso de librería de fecha y tiempo"""

from datetime import datetime

str_data = "12/6/2024"

"""
   d: día
   m: mes
   Y: año
"""
conversion = datetime.strptime(str_data, "%m/%d/%Y")
print("La fecha formateada es: {}".format(conversion))

"""Traer el mes de la fehca con formato de letras: strftime de datetime"""

conversion_mes = datetime.strftime(conversion, "%d %b del %Y")
print("Nuestra fecha con cambio del mes es el siguiente: {}".format(conversion_mes))

"""
    b: reemplaza a "m" para mostrar el mes literalmente
"""

