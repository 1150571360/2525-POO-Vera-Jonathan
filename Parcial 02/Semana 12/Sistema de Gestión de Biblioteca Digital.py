# sistema_biblioteca.py

# Clase Libro
class Libro:
    def _init_(self, titulo, autor, categoria, isbn):
        self.info = (titulo, autor)
        self.categoria = categoria
        self.isbn = isbn

    def _str_(self):
        return f"{self.info[0]} por {self.info[1]} | Categoría: {self.categoria} | ISBN: {self.isbn}"

# Clase Usuario
class Usuario:
    def _init_(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []

    def _str_(self):
        return f"Usuario: {self.nombre} | ID: {self.id_usuario}"

# Clase Biblioteca
class Biblioteca:
    def _init_(self):
        self.libros_disponibles = {}
        self.usuarios_registrados = {}
        self.ids_usuarios = set()

    def agregar_libro(self, libro):
        if libro.isbn in self.libros_disponibles:
            print("⚠️ El libro ya está registrado.")
        else:
            self.libros_disponibles[libro.isbn] = libro
            print(f"✅ Libro agregado: {libro}")

    def quitar_libro(self, isbn):
        if isbn in self.libros_disponibles:
            del self.libros_disponibles[isbn]
            print(f"🗑️ Libro con ISBN {isbn} eliminado.")
        else:
            print("⚠️ No se encontró el libro.")

    def registrar_usuario(self, usuario):
        if usuario.id_usuario in self.ids_usuarios:
            print("⚠️ ID de usuario ya registrado.")
        else:
            self.usuarios_registrados[usuario.id_usuario] = usuario
            self.ids_usuarios.add(usuario.id_usuario)
            print(f"✅ Usuario registrado: {usuario}")

    def dar_baja_usuario(self, id_usuario):
        if id_usuario in self.usuarios_registrados:
            del self.usuarios_registrados[id_usuario]
            self.ids_usuarios.remove(id_usuario)
            print(f"🗑️ Usuario con ID {id_usuario} eliminado.")
        else:
            print("⚠️ Usuario no encontrado.")

    def prestar_libro(self, id_usuario, isbn):
        if id_usuario not in self.usuarios_registrados:
            print("⚠️ Usuario no registrado.")
            return
        if isbn not in self.libros_disponibles:
            print("⚠️ Libro no disponible.")
            return
        usuario = self.usuarios_registrados[id_usuario]
        libro = self.libros_disponibles.pop(isbn)
        usuario.libros_prestados.append(libro)
        print(f"📚 Libro prestado: {libro.info[0]} a {usuario.nombre}")

    def devolver_libro(self, id_usuario, isbn):
        if id_usuario not in self.usuarios_registrados:
            print("⚠️ Usuario no registrado.")
            return
        usuario = self.usuarios_registrados[id_usuario]
        for libro in usuario.libros_prestados:
            if libro.isbn == isbn:
                usuario.libros_prestados.remove(libro)
                self.libros_disponibles[isbn] = libro
                print(f"🔄 Libro devuelto: {libro.info[0]}")
                return
        print("⚠️ El usuario no tiene este libro prestado.")

    def buscar_libros(self, criterio, valor):
        resultados = []
        for libro in self.libros_disponibles.values():
            if criterio == "titulo" and valor.lower() in libro.info[0].lower():
                resultados.append(libro)
            elif criterio == "autor" and valor.lower() in libro.info[1].lower():
                resultados.append(libro)
            elif criterio == "categoria" and valor.lower() in libro.categoria.lower():
                resultados.append(libro)
        print(f"🔍 Resultados de búsqueda por {criterio}='{valor}':")
        for r in resultados:
            print(f" - {r}")
        if not resultados:
            print("📭 No se encontraron coincidencias.")

    def listar_libros_prestados(self, id_usuario):
        if id_usuario not in self.usuarios_registrados:
            print("⚠️ Usuario no registrado.")
            return
        usuario = self.usuarios_registrados[id_usuario]
        print(f"📖 Libros prestados a {usuario.nombre}:")
        for libro in usuario.libros_prestados:
            print(f" - {libro}")
        if not usuario.libros_prestados:
            print("📭 No tiene libros prestados.")

# Prueba del sistema
if __name__ == "_main_":
    biblio = Biblioteca()

    libro1 = Libro("Cien Años de Soledad", "Gabriel García Márquez", "Novela", "ISBN001")
    libro2 = Libro("Python para Todos", "Charles Severance", "Programación", "ISBN002")

    biblio.agregar_libro(libro1)
    biblio.agregar_libro(libro2)

    usuario1 = Usuario("Jonathan Vera", "U001")
    usuario2 = Usuario("Ana Torres", "U002")

    biblio.registrar_usuario(usuario1)
    biblio.registrar_usuario(usuario2)

    biblio.prestar_libro("U001", "ISBN001")
    biblio.listar_libros_prestados("U001")
    biblio.buscar_libros("autor", "Gabriel")
    biblio.devolver_libro("U001", "ISBN001")
    biblio.quitar_libro("ISBN002")
    biblio.dar_baja_usuario("U002")


