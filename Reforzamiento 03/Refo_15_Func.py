"""Reforzamiento 15"""


"""15. Crea un módulo llamado generador.py que cumpla los siguientes requisitos:
        • Tendrá una función llamada leer_numero(). Esta función tomará 2
        valores: ini y fin, ingresado por consola. Que serán los límites de los
        números a crear.
        • Una vez la tengas los números, deberás crear una nueva función
        llamada generador, no recibirá ningún parámetro. Dentro usarás la
        función leer_numero():
        • En la cual se creará una lista donde los números que tendrá
        esta lista serán los números obtenidos en la primera
        función (respetando el ini y fin)
        • Esta función devolverá el cuadrado de todos esto números
        que están dentro de la lista.
        
        • Finalmente importando estas funciones respectivamente en el archivo
        main.py (principal) se mostrarán los números cuadrados"""

"""Funciones"""

def generador():
    list = []
    num_ini, num_fin = leer_numero()
    for i in range(num_ini, num_fin+1):
        list.append(i**2)
    print(list)



def leer_numero():
    ini = int(input("Ingrese el numero de inicio: "))
    fin = int(input("Ingrese el número de fin: "))
    return ini, fin

generador()
print(leer_numero())


