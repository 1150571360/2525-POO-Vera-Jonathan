import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry  # Instala con: pip install tkcalendar

# Crear ventana principal
root = tk.Tk()
root.title("Agenda Personal")
root.geometry("600x400")

# ================= FRAME DE ENTRADA =================
frame_entrada = tk.Frame(root, padx=10, pady=10)
frame_entrada.pack(fill="x")

# Etiquetas y campos de entrada
tk.Label(frame_entrada, text="Fecha:").grid(row=0, column=0, sticky="w")
date_entry = DateEntry(frame_entrada, date_pattern="dd/mm/yyyy")
date_entry.grid(row=0, column=1)

tk.Label(frame_entrada, text="Hora (HH:MM):").grid(row=1, column=0, sticky="w")
hora_entry = tk.Entry(frame_entrada)
hora_entry.grid(row=1, column=1)

tk.Label(frame_entrada, text="Descripción:").grid(row=2, column=0, sticky="w")
desc_entry = tk.Entry(frame_entrada, width=40)
desc_entry.grid(row=2, column=1)

# ================= FRAME DE BOTONES =================
frame_botones = tk.Frame(root, pady=10)
frame_botones.pack()

def agregar_evento():
    fecha = date_entry.get()
    hora = hora_entry.get()
    descripcion = desc_entry.get()
    if fecha and hora and descripcion:
        tree.insert("", "end", values=(fecha, hora, descripcion))
        hora_entry.delete(0, tk.END)
        desc_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Campos vacíos", "Por favor completa todos los campos.")

def eliminar_evento():
    seleccionado = tree.selection()
    if seleccionado:
        confirmar = messagebox.askyesno("Confirmar", "¿Eliminar el evento seleccionado?")
        if confirmar:
            tree.delete(seleccionado)
    else:
        messagebox.showinfo("Sin selección", "Selecciona un evento para eliminar.")

tk.Button(frame_botones, text="Agregar Evento", command=agregar_evento).grid(row=0, column=0, padx=5)
tk.Button(frame_botones, text="Eliminar Evento Seleccionado", command=eliminar_evento).grid(row=0, column=1, padx=5)
tk.Button(frame_botones, text="Salir", command=root.quit).grid(row=0, column=2, padx=5)

# ================= FRAME DE LISTA DE EVENTOS =================
frame_lista = tk.Frame(root)
frame_lista.pack(fill="both", expand=True)

tree = ttk.Treeview(frame_lista, columns=("Fecha", "Hora", "Descripción"), show="headings")
tree.heading("Fecha", text="Fecha")
tree.heading("Hora", text="Hora")
tree.heading("Descripción", text="Descripción")
tree.pack(fill="both", expand=True)

# Ejecutar la aplicación
root.mainloop()