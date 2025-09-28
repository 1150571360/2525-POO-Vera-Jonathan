import tkinter as tk
from tkinter import messagebox

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Lista de Tareas")
ventana.geometry("400x400")

# Lista para almacenar las tareas como diccionarios
tareas = []

# Función para añadir una nueva tarea
def añadir_tarea(event=None):
    texto = entrada.get().strip()
    if texto:
        tareas.append({"texto": texto, "completada": False})
        entrada.delete(0, tk.END)
        actualizar_lista()
    else:
        messagebox.showwarning("Campo vacío", "Por favor escribe una tarea.")

# Función para marcar una tarea como completada
def marcar_completada():
    seleccion = lista.curselection()
    if seleccion:
        index = seleccion[0]
        tareas[index]["completada"] = True
        actualizar_lista()
    else:
        messagebox.showinfo("Sin selección", "Selecciona una tarea para marcar como completada.")

# Función para eliminar una tarea
def eliminar_tarea():
    seleccion = lista.curselection()
    if seleccion:
        index = seleccion[0]
        tareas.pop(index)
        actualizar_lista()
    else:
        messagebox.showinfo("Sin selección", "Selecciona una tarea para eliminar.")

# Función para actualizar visualmente la lista de tareas
def actualizar_lista():
    lista.delete(0, tk.END)
    for tarea in tareas:
        texto = tarea["texto"]
        if tarea["completada"]:
            texto += " ✔"
        lista.insert(tk.END, texto)

# Evento adicional: doble clic para alternar estado de completada
def doble_clic(event):
    seleccion = lista.curselection()
    if seleccion:
        index = seleccion[0]
        tareas[index]["completada"] = not tareas[index]["completada"]
        actualizar_lista()

# Crear campo de entrada para nuevas tareas
entrada = tk.Entry(ventana, font=("Arial", 12))
entrada.pack(pady=10)
entrada.bind("<Return>", añadir_tarea)  # Permitir añadir con Enter

# Botón para añadir tarea
boton_añadir = tk.Button(ventana, text="Añadir Tarea", command=añadir_tarea)
boton_añadir.pack(pady=5)

# Botón para marcar como completada
boton_completar = tk.Button(ventana, text="Marcar como Completada", command=marcar_completada)
boton_completar.pack(pady=5)

# Botón para eliminar tarea
boton_eliminar = tk.Button(ventana, text="Eliminar Tarea", command=eliminar_tarea)
boton_eliminar.pack(pady=5)

# Componente Listbox para mostrar las tareas
lista = tk.Listbox(ventana, font=("Arial", 12), selectmode=tk.SINGLE)
lista.pack(pady=10, fill=tk.BOTH, expand=True)
lista.bind("<Double-Button-1>", doble_clic)  # Evento adicional

# Ejecutar la aplicación
ventana.mainloop()