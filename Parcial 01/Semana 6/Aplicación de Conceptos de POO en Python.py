# Clase base: Persona
class Persona:
    """
    Clase base que representa una persona con nombre y cédula.
    Se aplican atributos encapsulados.
    """
    def __init__(self, nombre, cedula):
        self.__nombre = nombre       # Encapsulación
        self.__cedula = cedula

    def obtener_info(self):
        return f"Nombre: {self.__nombre} | Cédula: {self.__cedula}"

    def saludar(self, mensaje="¡Hola!"):
        """
        Metodo con parámetro opcional → polimorfismo.
        """
        return f"{mensaje} Soy {self.__nombre}."


# Clase derivada: Estudiante
class Estudiante(Persona):
    """
    Hereda de Persona. Representa a un estudiante con una carrera y materias inscritas.
    """
    def __init__(self, nombre, cedula, carrera):
        super().__init__(nombre, cedula)
        self.__carrera = carrera
        self.__materias = []

    def agregar_materia(self, *materias):
        """
        Polimorfismo usando argumentos múltiples (*args).
        """
        self.__materias.extend(materias)

    # Sobrescribir metodo heredado → polimorfismo
    def obtener_info(self):
        info_base = super().obtener_info()
        return f"{info_base} | Carrera: {self.__carrera}"

    def listar_materias(self):
        return ", ".join(self.__materias) if self.__materias else "Sin materias registradas."


# Crear instancias y demostrar funcionalidad
est1 = Estudiante("Jonathan Vera", "1104123456", "Ingeniería TI")
est1.agregar_materia("POO", "Sistemas Operativos", "Física")

# Salida
print(est1.obtener_info())                      # Polimorfismo: metodo sobrescrito
print(est1.saludar("Saludos cordiales"))        # Polimorfismo: argumento opcional
print("Materias inscritas:", est1.listar_materias())
