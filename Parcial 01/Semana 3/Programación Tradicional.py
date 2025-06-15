def ingresar_temperaturas():
    temperaturas = []
    for i in range(7):
        temp = float(input(f"Ingrese la temperatura del día {i+1}: "))
        temperaturas.append(temp)
    return temperaturas

def calcular_promedio(temperaturas):
    return sum(temperaturas) / len(temperaturas)

# Uso del programa
temperaturas_semanales = ingresar_temperaturas()
promedio = calcular_promedio(temperaturas_semanales)
print(f"Elpromedio semanal de temperatura es: {promedio:.2f}°C")