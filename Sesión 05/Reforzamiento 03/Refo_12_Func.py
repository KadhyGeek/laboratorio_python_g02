"""Reforzamiento 12"""


"""12. Realizar una clase que administre una agenda. Se debe almacenar en
un diccionario dentro de una lista para cada contacto el nombre, el
teléfono, email y DNI. Deberá tener los siguientes métodos:
Añadir contacto
Mostrar contactos
Buscar contacto
(Por DNI)"""

"""Funciones"""


# creamos nuestra clase agenda
class Agenda:
    # iniciamos nuestra clase
    def __init__(self):
        # crearemos una lista donde guardaremos los datos de nuestra agenda
        self.contactos = []

    # menu del programa
    def menu(self):
        print()
        menu = [
            ['Agenda Personal'],
            ['1. Añadir Contacto', "anadir"],
            ['2. Lista de contactos'],
            ['3. Buscar contacto'],
            ['4. Cerrar agenda']
        ]

        for x in range(5):
            print(menu[x][0])

        opcion = int(input("Introduzca la opción deseada: "))
        if opcion == 1:
            self.anadir()
        elif opcion == 2:
            self.mostrar()
        elif opcion == 3:
            self.buscar()
        elif opcion == 4:
            print("Saliendo de la agenda ...")
            exit()

        # volvemos a llamar al menú
        self.menu()

    # función para añadir un contacto
    def anadir(self):
        print("---------------------")
        print("Añadir nuevo contacto")
        print("---------------------")
        dni = input("Introduzca el DNI: ")
        nom = input("Introduzca el nombre: ")
        telf = int(input("Introduzca el teléfono: "))
        email = input("Introduzca el email: ")
        self.contactos.append({'dni': dni, 'nombre': nom, 'telf': telf, 'email': email})

    # función para imprimir la lista de contactos
    # En este caso imprimiremos solo los nombres de los contactos
    # con ellos podremos buscar luego un contacto
    def mostrar(self):
        print("------------------")
        print("Lista de contactos")
        print("------------------")
        if len(self.contactos) == 0:
            print("No hay ningún contacto en la agenda")
        else:
            for x in range(len(self.contactos)):
                print("  DNI  "," ","  Nombre   "," ","   Telefono  "," ","  Email  ")
                print(self.contactos[x]['dni']," ",self.contactos[x]['nombre']," ",self.contactos[x]['telf']," ",self.contactos[x]['email'])

    # función para buscar un contacto a través del nombre
    def buscar(self):
        print("---------------------")
        print("Buscador de contactos")
        print("---------------------")
        dni = input("Introduzca el DNI del contacto: ")
        for x in range(len(self.contactos)):
            if dni == self.contactos[x]['dni']:
                print("Datos del contacto")
                print("Dni: ", self.contactos[x]['dni'])
                print("Nombre: ", self.contactos[x]['nombre'])
                print("Teléfono: ", self.contactos[x]['telf'])
                print("E-mail: ", self.contactos[x]['email'])
                return x

# bloque principal
agenda = Agenda()
agenda.menu()