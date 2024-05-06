"""
    Programación orientada a objetos en Python
    Participación

Requerimientos:

- Crear clase alumno
- Debe tener un atributo de nacionalidad con valor "Peruano"
- Crear un método que indicará el promedio del alumno (mostrar en pantalla el promedio)
- Crear un método que indicará si el alumno está aprobado (>=11)
 o no de acuerdo a su promedio  (mostrar en pantalla el mensaje)
- Tendrá 3 notas, la nota inicial será de 0 para todos
- Obtener el nombre y distrito de residencia (mostrar en pantalla estos valores)

"""
class Alumno:
    """Atributos"""
    nacionalidad = "peruano"
    def __init__(self, nota_1, nota_2, nota_3):
        self.nota_1 = nota_1
        self.nota_2 = nota_2
        self.nota_3 = nota_3
        self.promedio = 0

    """Métodos: So las funciones de la clase"""
    def promedio_nota(self):

        self.promedio = round(((self.nota_1 + self.nota_2 + self.nota_3)/3),2)
        if self.promedio >= 11:
            print("aprobado")
        else:
            print("Desaprobado")


Alumno_1 = Alumno(20, 5,10)

#print( "el promedio del alumno es: {}".format( Alumno_1.promedio() ) )
Alumno_1.promedio_nota()
print(Alumno_1.promedio)