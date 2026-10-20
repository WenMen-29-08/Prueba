# Clase madre
class Empleado:
    def __init__(self, nombre, identificacion, salario):
        self.nombre = nombre
        self.identificacion = identificacion
        self.salario = salario

    def mostrar_datos(self):
        print("Nombre:", self.nombre)
        print("Identificación:", self.identificacion)
        print("Salario:", self.salario)

    def trabajar(self):
        print(self.nombre, "está trabajando")


# Clase hija Desarrollador
class Desarrollador(Empleado):
    def __init__(self, nombre, identificacion, salario, lenguaje_programacion):
        super().__init__(nombre, identificacion, salario)
        self.lenguaje_programacion = lenguaje_programacion

    def programar(self):
        print(self.nombre, "está programando en", self.lenguaje_programacion)


# Clase hija Diseñador
class Diseñador(Empleado):
    def __init__(self, nombre, identificacion, salario, herramienta_diseño):
        super().__init__(nombre, identificacion, salario)
        self.herramienta_diseño = herramienta_diseño

    def disenar(self):
        print(self.nombre, "está diseñando con", self.herramienta_diseño)


# Clase hija Instructor
class Instructor(Empleado):
    def __init__(self, nombre, identificacion, salario, especialidad):
        super().__init__(nombre, identificacion, salario)
        self.especialidad = especialidad

    def orientar_formacion(self):
        print(self.nombre, "está orientando formación en", self.especialidad)


# Crear objetos
desarrollador1 = Desarrollador("Jose", 12345, 3000000, "java")
disenador1 = Diseñador("Daniela", 67890, 2800000, "html")
instructor1 = Instructor("Alberto", 54321, 3200000, "Desarrollo de base de datos")


# Mostrar información y ejecutar métodos
print("----- PROGRAMADOR -----")
desarrollador1.mostrar_datos()
desarrollador1.trabajar()
desarrollador1.programar()

print("\n----- CREATIVIDAD -----")
disenador1.mostrar_datos()
disenador1.trabajar()
disenador1.disenar()

print("\n----- INSTRUCTOR -----")
instructor1.mostrar_datos()
instructor1.trabajar()
instructor1.orientar_formacion()