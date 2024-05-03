"""Uso de librería de fecha y tiempo"""

"""
    Conversión total del tiempo
"""

from datetime import datetime

"""Uso del método timestamp: suma total en segundo de la fecha"""

time_now = datetime.strptime("2024/12/15 20:30:00", "%Y/%m/%d %H:%M:%S").timestamp()

print("La conversión de nuestro valor time_now es: {}".format(time_now))
