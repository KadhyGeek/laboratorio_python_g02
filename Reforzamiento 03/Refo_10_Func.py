"""Reforzamiento 10"""


"""10. Crear una clase llamada Alumno que tenga como atributos el nombre,
edad y la nota final del alumno. Crear los métodos para inicializar sus
atributos, otro para imprimirlos y un método para mostrar un mensaje
con el resultado de la nota y si ha aprobado (mayor o igual a 11) o no el
alumno.Instanciar la clase por lo menos 3 veces (3 alumnos)"""

"""Funciones"""

class Alumno:
    def __init__(self, nombre, edad, nota_final):
        self.nombre = nombre
        self.edad = edad
        self.nota_final = nota_final

    def imprimir(self):
        print(f" Hola {self.nombre} tu edad es {self.edad} y tu nota es {self.nota_final}, por ello estas {self.resultado()}")

    def resultado(self):
        if self.nota_final >= 11:
            return "Aprobado"
        elif self.nota_final < 11:
            return "Reprovado"


alumno_1 = Alumno("Ana", "23", 10)
alumno_2 = Alumno("Eduardo", "13", 20)
alumno_1.imprimir()
alumno_1.resultado()
alumno_2.imprimir()
alumno_2.resultado()
alumno_3 = Alumno("Carolina", "34", 11)
alumno_3.imprimir()
alumno_3.resultado()
