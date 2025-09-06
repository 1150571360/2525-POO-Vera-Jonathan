class Producto:
    def init(self, id_producto, nombre, cantidad, precio):
        self.id = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def actualizarcantidad(self, nuevacantidad):
        self.cantidad = nueva_cantidad

    def actualizarprecio(self, nuevoprecio):
        self.precio = nuevo_precio

    def obtener_info(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "cantidad": self.cantidad,
            "precio": self.precio
        }

    def str(self):
        return f"ID: {self.id} | Nombre: {self.nombre} | Cantidad: {self.cantidad} | Precio: ${self.precio:.2f}"

import json
from producto import Producto

class Inventario:
    def init(self):
        self.productos = {}  # Diccionario: clave = ID, valor = Producto

    def añadir_producto(self, producto):
        if producto.id in self.productos:
            print("❌ El ID ya existe.")
        else:
            self.productos[producto.id] = producto
            print("✅ Producto añadido.")

    def eliminarproducto(self, idproducto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            print("🗑️ Producto eliminado.")
        else:
            print("❌ Producto no encontrado.")

    def actualizarproducto(self, idproducto, cantidad=None, precio=None):
        producto = self.productos.get(id_producto)
        if producto:
            if cantidad is not None:
                producto.actualizar_cantidad(cantidad)
            if precio is not None:
                producto.actualizar_precio(precio)
            print("🔄 Producto actualizado.")
        else:
            print("❌ Producto no encontrado.")

    def buscarpornombre(self, nombre):
        encontrados = [p for p in self.productos.values() if p.nombre.lower() == nombre.lower()]
        if encontrados:
            for p in encontrados:
                print(p)
        else:
            print("🔍 No se encontraron productos con ese nombre.")

    def mostrar_todos(self):
        if self.productos:
            for producto in self.productos.values():
                print(producto)
        else:
            print("📦 Inventario vacío.")

    def guardarenarchivo(self, archivo):
        with open(archivo, 'w') as f:
            json.dump({id: p.obtener_info() for id, p in self.productos.items()}, f, indent=4)
        print("💾 Inventario guardado.")

    def cargardesdearchivo(self, archivo):
        try:
            with open(archivo, 'r') as f:
                datos = json.load(f)
                for id, info in datos.items():
                    self.productos[id] = Producto(info['id'], info['nombre'], info['cantidad'], info['precio'])
            print("📂 Inventario cargado.")
        except FileNotFoundError:
            print("⚠️ Archivo no encontrado. Se iniciará un inventario vacío.")


from producto import Producto
from inventario import Inventario


def mostrar_menu():
    print("\n📋 MENÚ DE INVENTARIO")
    print("1. Añadir producto")
    print("2. Eliminar producto")
    print("3. Actualizar producto")
    print("4. Buscar producto por nombre")
    print("5. Mostrar todos los productos")
    print("6. Guardar inventario")
    print("7. Cargar inventario")
    print("8. Salir")


inventario = Inventario()
archivo = "inventario.json"

while True:
    mostrar_menu()
    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        id_producto = input("ID: ")
        nombre = input("Nombre: ")
        cantidad = int(input("Cantidad: "))
        precio = float(input("Precio: "))
        producto = Producto(id_producto, nombre, cantidad, precio)
        inventario.añadir_producto(producto)

    elif opcion == "2":
        id_producto = input("ID del producto a eliminar: ")
        inventario.eliminarproducto(idproducto)

    elif opcion == "3":
        id_producto = input("ID del producto a actualizar: ")
        cantidad = input("Nueva cantidad (dejar vacío si no aplica): ")
        precio = input("Nuevo precio (dejar vacío si no aplica): ")
        inventario.actualizar_producto(
            id_producto,
            cantidad=int(cantidad) if cantidad else None,
            precio=float(precio) if precio else None
        )

    elif opcion == "4":
        nombre = input("Nombre del producto: ")
        inventario.buscarpornombre(nombre)

    elif opcion == "5":
        inventario.mostrar_todos()

    elif opcion == "6":
        inventario.guardarenarchivo(archivo)

    elif opcion == "7":
        inventario.cargardesdearchivo(archivo)

    elif opcion == "8":
        print("👋 Saliendo del sistema.")
        break

    else:
        print("❌ Opción inválida.")