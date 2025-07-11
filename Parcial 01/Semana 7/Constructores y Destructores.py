class Estudiante:
    def __init__(self, nombre, carrera):
        """
        Constructor: se activa al crear el objeto.
        Inicializa el nombre y la carrera del estudiante, y abre un archivo de registro.
        """
        self.nombre = nombre
        self.carrera = carrera
        self.registro = open(f"{self.nombre}_registro.txt", "w")
        self.registro.write(f"Estudiante: {self.nombre}\nCarrera: {self.carrera}\n")
        print(f"[+] Registro de estudiante '{self.nombre}' creado.")

    def agregar_nota(self, materia, nota):
        """
        Añade una nota al registro del estudiante.
        """
        self.registro.write(f"Materia: {materia} - Nota: {nota}\n")
        print(f"[~] Se agregó la nota de {materia}: {nota}")

    def __del__(self):
        """
        Destructor: se ejecuta al destruir el objeto.
        Cierra el archivo de registro del estudiante.
        """
        if self.registro and not self.registro.closed:
            self.registro.write("Fin del registro académico.\n")
            self.registro.close()
            print(f"[-] Registro de '{self.nombre}' cerrado.")