class Pelicula:
    def __init__(self, titulo, duracion, genero):
        self.titulo = titulo
        self.duracion = duracion
        self.genero = genero

    def mostrar_info(self):
        return f"{self.to} ({self.duracion} min)"


class Sala:
    def __init__(self, numero_sala, capacidad):
        self.numero_sala = numero_sala
        self.capacidad = capacidad
        self.asientos_ocupados = 0

    def reservar_asiento(self, cantidad):
        if self.asientos_ocupados + cantidad <= self.capacidad:
            self.asientos_ocupados += cantidad
            return True
        return False


class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre


class Reserva:
    def __init__(self, cliente, pelicula, sala, cantidad):
        self.cliente = cliente
        self.pelicula = pelicula
        self.sala = sala
        self.cantidad = cantidad

    def realizar_reserva(self):
        if self.sala.reservar_asiento(self.cantidad):
            print(f"Reserva exitosa para {self.cliente.nombre}: {self.pelicula.titulo} ({self.cantidad} asiento/s)")
        else:
            print("No hay suficientes asientos disponibles.")