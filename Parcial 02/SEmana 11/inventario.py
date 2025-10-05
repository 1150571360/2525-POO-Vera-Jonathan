# Clase Inventario: gestiona los productos usando un diccionario y permite guardar/cargar desde archivo.

import json
from producto import Producto

class Inventario:
    def _init_(self):
        self.productos = {}  # Diccionario con ID como clave y Producto como valor

    def añadir_producto(self, producto):
        if producto.get_id() in self.productos:
            print("❌ Error: Ya existe un producto con ese ID.")
        else:
            self.productos[producto.get_id()] = producto
            print("✅ Producto añadido correctamente.")

    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            print("🗑️ Producto eliminado.")
        else:
            print("❌ Producto no encontrado.")

    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        if id_producto in self.productos:
            producto = self.productos[id_producto]
            if nueva_cantidad is not None:
                producto.set_cantidad(nueva_cantidad)
            if nuevo_precio is not None:
                producto.set_precio(nuevo_precio)
            print("🔄 Producto actualizado.")
        else:
            print("❌ Producto no encontrado.")

    def buscar_por_nombre(self, nombre_busqueda):
        encontrados = [p for p in self.productos.values() if nombre_busqueda.lower() in p.get_nombre().lower()]
        if encontrados:
            print("🔍 Resultados encontrados:")
            for p in encontrados:
                print(p)
        else:
            print("❌ No se encontraron productos con ese nombre.")

    def mostrar_todos(self):
        if not self.productos:
            print("📦 El inventario está vacío.")
        else:
            print("📋 Productos en inventario:")
            for p in self.productos.values():
                print(p)

    def guardar_en_archivo(self, nombre_archivo):
        try:
            with open(nombre_archivo, "w") as f:
                json.dump({id: p.to_dict() for id, p in self.productos.items()}, f, indent=4)
            print("💾 Inventario guardado correctamente.")
        except Exception as e:
            print(f"⚠️ Error al guardar: {e}")

    def cargar_desde_archivo(self, nombre_archivo):
        try:
            with open(nombre_archivo, "r") as f:
                data = json.load(f)
                self.productos = {id: Producto.from_dict(p) for id, p in data.items()}
            print("📂 Inventario cargado correctamente.")
        except FileNotFoundError:
            print("📁 Archivo no encontrado. Se iniciará un inventario vacío.")
        except Exception as e:
            print(f"⚠️ Error al cargar: {e}")