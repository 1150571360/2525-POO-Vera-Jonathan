# Interfaz de usuario en consola para interactuar con el inventario.

from producto import Producto
from inventario import Inventario

def menu():
    inventario = Inventario()
    inventario.cargar_desde_archivo("inventario.json")

    while True:
        print("\n📌 MENÚ DE INVENTARIO")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todos los productos")
        print("6. Guardar inventario en archivo")
        print("7. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            try:
                id_producto = input("ID del producto: ")
                nombre = input("Nombre: ")
                cantidad = int(input("Cantidad: "))
                precio = float(input("Precio: "))
                nuevo_producto = Producto(id_producto, nombre, cantidad, precio)
                inventario.añadir_producto(nuevo_producto)
            except ValueError:
                print("⚠️ Error: Entrada inválida.")

        elif opcion == "2":
            id_producto = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == "3":
            id_producto = input("ID del producto a actualizar: ")
            cantidad_input = input("Nueva cantidad (dejar vacío para no cambiar): ")
            precio_input = input("Nuevo precio (dejar vacío para no cambiar): ")

            nueva_cantidad = int(cantidad_input) if cantidad_input else None
            nuevo_precio = float(precio_input) if precio_input else None

            inventario.actualizar_producto(id_producto, nueva_cantidad, nuevo_precio)

        elif opcion == "4":
            nombre = input("Nombre a buscar: ")
            inventario.buscar_por_nombre(nombre)

        elif opcion == "5":
            inventario.mostrar_todos()

        elif opcion == "6":
            inventario.guardar_en_archivo("inventario.json")

        elif opcion == "7":
            inventario.guardar_en_archivo("inventario.json")
            print("👋 Saliendo del sistema...")
            break

        else:
            print("❌ Opción inválida. Intenta nuevamente.")

if _name_ == "_main_":
    menu()