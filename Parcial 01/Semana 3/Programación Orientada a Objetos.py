class ClimaSemanal:
    def __init__(self):
        self.temperaturas = []

    def ingresar_temperatura(self, temp):
        self.temperaturas.append(temp)

    def calcular_promedio(self):
        return sum(self.temperaturas) / len(self.temperaturas)

# Uso del programa
clima = ClimaSemanal()
for i in range(7):
    temp = float(input(f"Ingrese la temperatura del día {i+1}: "))
    clima.ingresar_temperatura(temp)

    promedio = clima.calcular_promedio()
    print(f"El promedio semanal de temperatura es: {promedio:.2f}°C")