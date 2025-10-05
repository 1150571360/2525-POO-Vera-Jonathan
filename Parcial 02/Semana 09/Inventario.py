# Clase Inventario: gestiona una lista de productos y permite operaciones sobre ellos.

from producto import Producto

class Inventario:
    def _init_(self):
        self.productos = []

    def añadir_producto(self, producto):
        # Verifica que el ID sea único antes de añadir
        for p in self.productos:
            if p.get_id() == producto.get_id():
                print("❌ Error: Ya existe un producto con ese ID.")
                return
        self.productos.append(producto)
        print("✅ Producto añadido correctamente.")

    def eliminar_producto(self, id_producto):
        for p in self.productos:
            if p.get_id() == id_producto:
                self.productos.remove(p)
                print("🗑️ Producto eliminado.")
                return
        print("❌ Producto no encontrado.")

    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        for p in self.productos:
            if p.get_id() == id_producto:
                if nueva_cantidad is not None:
                    p.set_cantidad(nueva_cantidad)
                if nuevo_precio is not None:
                    p.set_precio(nuevo_precio)
                print("🔄 Producto actualizado.")
                return
        print("❌ Producto no encontrado.")

    def buscar_por_nombre(self, nombre_busqueda):
        resultados = [p for p in self.productos if nombre_busqueda.lower() in p.get_nombre().lower()]
        if resultados:
            print("🔍 Resultados encontrados:")
            for p in resultados:
                print(p)
        else:
            print("❌ No se encontraron productos con ese nombre.")

    def mostrar_todos(self):
        if not self.productos:
            print("📦 El inventario está vacío.")
        else:
            print("📋 Productos en inventario:")
            for p in self.productos:
                print(p)