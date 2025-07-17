# Programa para calcular el área de un círculo dado su radio
# Utiliza distintos tipos de datos (int, float, string, bool)
# Desarrollado siguiendo la convención snake_case para claridad

import math  # Librería para funciones matemáticas como pi

def calcular_area_circulo():
    mensaje_bienvenida = "Bienvenido a la calculadora de área de círculos"
    print(mensaje_bienvenida)

    # Solicita al usuario que ingrese el radio del círculo
    radio_input = input("Ingresa el radio del círculo (cm): ")

    # Conversión de datos: de string a float
    try:
        radio_cm = float(radio_input)  # Se espera un número decimal o entero
        es_radio_valido = radio_cm > 0  # Verificamos que sea un valor positivo (booleano)

        if es_radio_valido:
            area = math.pi * (radio_cm ** 2)  # Fórmula del área de un círculo
            print(f"El área del círculo es {area:.2f} cm²")
        else:
            print("X El radio debe ser un número positivo.")
    except ValueError:
        print("X Entrada no válida. Debes ingresar un número.")

# Ejecuta la función principal
calcular_area_circulo()