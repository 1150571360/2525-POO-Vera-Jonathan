import os
from datetime import datetime

# Función para mostrar el contenido del script
def mostrar_codigo(ruta_script):
    ruta_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_absoluta, 'r') as archivo:
            print(f"\n📄 Código de {ruta_script}\n{'='*40}")
            print(archivo.read())
            registrar_actividad(ruta_script)
    except FileNotFoundError:
        print("⚠️ El archivo no se encontró.")
    except Exception as e:
        print(f"⚠️ Ocurrió un error al leer el archivo: {e}")

# Función para registrar la actividad en un log
def registrar_actividad(nombre_script):
    log_path = os.path.join(os.path.dirname(__file__), "registro_log.txt")
    with open(log_path, 'a') as log:
        log.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Script revisado: {nombre_script}\n")

# Diccionario general con materias y scripts relacionados
materias = {
    "1": ("📊 Estadística", {
        "1": "ESTADISTICA/1.1. Media y Varianza.py",
        "2": "ESTADISTICA/1.2. Histogramas.py"
    }),
    "2": ("🧬 Programación Orientada a Objetos", {
        "1": "POO/2.1. Clases y Objetos.py",
        "2": "POO/2.2. Herencia.py"
    }),
    "3": ("🖥️ Sistemas Operativos", {
        "1": "SO/3.1. Planificación de procesos.py",
        "2": "SO/3.2. Memoria virtual.py"
    }),
    "4": ("📐 Matemáticas", {
        "1": "MATEMATICAS/4.1. Álgebra lineal.py",
        "2": "MATEMATICAS/4.2. Derivadas.py"
    }),
    "5": ("🌌 Física", {
        "1": "FISICA/5.1. Movimiento rectilíneo.py"
    }),
    "6": ("🗣️ Inglés técnico", {
        "1": "INGLES/6.1. Glosario de programación en inglés.py"
    })
}

# Menú principal para seleccionar materia
def mostrar_menu_materias():
    while True:
        print("\n📚 Menú de materias")
        print("-" * 40)
        for key, (nombre, _) in materias.items():
            print(f"{key}. {nombre}")
        print("0. ❌ Salir")
        print("-" * 40)

        eleccion = input("Selecciona una materia para ver sus tareas: ")
        if eleccion == "0":
            print("👋 Saliendo del organizador académico.")
            break
        elif eleccion in materias:
            nombre_materia, tareas = materias[eleccion]
            mostrar_menu_tareas(nombre_materia, tareas)
        else:
            print("❗ Opción inválida. Intenta de nuevo.")

# Menú de scripts dentro de una materia
def mostrar_menu_tareas(nombre_materia, tareas):
    while True:
        print(f"\n🔎 Tareas - {nombre_materia}")
        for key, ruta in tareas.items():
            print(f"{key}. 📂 {ruta}")
        print("0. 🔙 Volver")

        eleccion = input("Selecciona una tarea para visualizar: ")
        if eleccion == "0":
            break
        elif eleccion in tareas:
            ruta_script = os.path.join(os.path.dirname(__file__), tareas[eleccion])
            mostrar_codigo(ruta_script)
        else:
            print("❗ Opción inválida.")

# Punto de ejecución
if __name__ == "__main__":
    mostrar_menu_materias()