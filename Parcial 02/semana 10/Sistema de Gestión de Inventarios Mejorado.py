import os

class Inventario:
    def init(self, archivo='inventario.txt'):
        self.archivo = archivo
        self.productos = {}
        self.cargardesdearchivo()

    def cargardesdearchivo(self):
        """Carga los productos desde el archivo de texto al diccionario."""
        try:
            with open(self.archivo, 'r') as f:
                for linea in f:
                    partes = linea.strip().split(',')
                    if len(partes) == 3:
                        nombre, cantidad, precio = partes
                        self.productos[nombre] = {
                            'cantidad': int(cantidad),
                            'precio': float(precio)
                        }
            print("Inventario cargado correctamente.")
        except FileNotFoundError:
            print("Archivo no encontrado. Se creará uno nuevo al guardar.")
        except PermissionError:
            print("Permiso denegado para leer el archivo.")
        except Exception as e:
            print(f"Error inesperado al cargar el archivo: {e}")

    def guardarenarchivo(self):
        """Guarda el contenido del inventario en el archivo."""
        try:
            with open(self.archivo, 'w') as f:
                for nombre, datos in self.productos.items():
                    f.write(f"{nombre},{datos['cantidad']},{datos['precio']}\n")
            print("Inventario guardado exitosamente.")
        except PermissionError:
            print("Permiso denegado para escribir en el archivo.")
        except Exception as e:
            print(f"Error inesperado al guardar el archivo: {e}")

    def agregar_producto(self, nombre, cantidad, precio):
        """Agrega un nuevo producto al inventario."""
        if nombre in self.productos:
            print("El producto ya existe. Usa actualizar_producto.")
            return
        self.productos[nombre] = {'cantidad': cantidad, 'precio': precio}
        self.guardarenarchivo()
        print(f"Producto '{nombre}' agregado correctamente.")

    def actualizar_producto(self, nombre, cantidad=None, precio=None):
        """Actualiza la cantidad o precio de un producto existente."""
        if nombre not in self.productos:
            print("Producto no encontrado.")
            return
        if cantidad is not None:
            self.productos[nombre]['cantidad'] = cantidad
        if precio is not None:
            self.productos[nombre]['precio'] = precio
        self.guardarenarchivo()
        print(f"Producto '{nombre}' actualizado correctamente.")

    def eliminar_producto(self, nombre):
        """Elimina un producto del inventario."""
        if nombre in self.productos:
            del self.productos[nombre]
            self.guardarenarchivo()
            print(f"Producto '{nombre}' eliminado correctamente.")
        else:
            print("Producto no encontrado.")

    def mostrar_inventario(self):
        """Muestra todos los productos en consola."""
        if not self.productos:
            print("Inventario vacío.")
            return
        print("Inventario actual:")
        for nombre, datos in self.productos.items():
            print(f" - {nombre}: {datos['cantidad']} unidades, ${datos['precio']:.2f}")