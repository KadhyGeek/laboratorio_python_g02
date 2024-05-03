"""Uso de librería de fecha y tiempo"""

from datetime import datetime, date

"""Obtener la fecha catual"""

fecha = date.today()
print("La fecha a manejar es la siguiente: {}".format(fecha))

tiempo = datetime.now()
print(tiempo)

anio = tiempo.year
mes = tiempo.month
dia = tiempo.day

print("Año actual: {}".format(anio))
print("Mes actual: {}".format(mes))
print("Día actual: {}".format(dia))

"""Uso del datetime para extraer la hora, el minuto y el segundo"""

hora = tiempo.hour
minuto = tiempo.minute
segundo = tiempo.second

print("La hora exacta son las {} horas con {} minutos y {} segundos".format(hora, minuto,segundo))
