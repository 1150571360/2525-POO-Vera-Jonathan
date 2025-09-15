import tkinter as tk
from tkinter import messagebox

# Función que se ejecuta al presionar el botón "Agregar"
def agregar_dato():
    dato = entrada.get()
    if dato.strip() != "":
        lista_datos.insert(tk.END, dato)  # Agrega el dato a la lista
        entrada.delete(0, tk.END)         # Limpia el campo de texto
    else:
        messagebox.showwarning("Campo vacío", "Por favor ingrese algún dato.")

# Función que se ejecuta al presionar el botón "Limpiar"
def limpiar_datos():
    lista_datos.delete(0, tk.END)         # Borra todos los elementos de la lista
    entrada.delete(0, tk.END)             # Limpia el campo de texto

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Registro de Datos - Aplicación GUI Básica")
ventana.geometry("400x350")
ventana.resizable(False, False)

# Etiqueta de instrucción
etiqueta = tk.Label(ventana, text="Ingrese un dato:", font=("Arial", 12))
etiqueta.pack(pady=10)

# Campo de texto para ingresar datos
entrada = tk.Entry(ventana, width=40, font=("Arial", 11))
entrada.pack(pady=5)

# Botón para agregar datos
boton_agregar = tk.Button(ventana, text="Agregar", command=agregar_dato, bg="#4CAF50", fg="white", width=15)
boton_agregar.pack(pady=5)

# Botón para limpiar datos
boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar_datos, bg="#f44336", fg="white", width=15)
boton_limpiar.pack(pady=5)

# Lista para mostrar los datos ingresados
lista_datos = tk.Listbox(ventana, width=50, height=10, font=("Arial", 10))
lista_datos.pack(pady=10)

# Ejecutar la aplicación
ventana.mainloop()

