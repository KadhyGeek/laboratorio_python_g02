"""Uso de librería de fecha y tiempo"""

"""
    Conversión de fechas
"""

import datetime

fecha_1 = datetime.datetime(2023, 4, 20)  # Tipo de dato datetime
fecha_2 = datetime.datetime(2023, 4, 12)  # Tipo de dato datetime

if fecha_1 == fecha_2:
    print("Nacieron el mismo día")
elif fecha_1 > fecha_2:
    print("El niño 2 es mayor que el niño 1")
else:
    print("El niño 1 es mayor que el niño 2")
