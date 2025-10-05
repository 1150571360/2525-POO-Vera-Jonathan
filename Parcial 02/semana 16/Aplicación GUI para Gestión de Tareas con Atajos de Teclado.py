import tkinter as tk
from tkinter import messagebox

class GestorTareas:
    def _init_(self, root):
        self.root = root
        self.root.title("📝 Gestor de Tareas")
        self.root.geometry("400x400")
        self.root.resizable(False, False)

        # Campo de entrada
        self.entry_tarea = tk.Entry(root, font=("Arial", 12))
        self.entry_tarea.pack(pady=10)
        self.entry_tarea.focus()

        # Lista de tareas
        self.lista_tareas = tk.Listbox(root, font=("Arial", 12), selectmode=tk.SINGLE)
        self.lista_tareas.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Botones
        frame_botones = tk.Frame(root)
        frame_botones.pack(pady=5)

        btn_añadir = tk.Button(frame_botones, text="➕ Añadir", command=self.añadir_tarea)
        btn_añadir.grid(row=0, column=0, padx=5)

        btn_completar = tk.Button(frame_botones, text="✅ Completar", command=self.marcar_completada)
        btn_completar.grid(row=0, column=1, padx=5)

        btn_eliminar = tk.Button(frame_botones, text="🗑️ Eliminar", command=self.eliminar_tarea)
        btn_eliminar.grid(row=0, column=2, padx=5)

        # Atajos de teclado
        self.root.bind("<Return>", lambda event: self.añadir_tarea())
        self.root.bind("<c>", lambda event: self.marcar_completada())
        self.root.bind("<d>", lambda event: self.eliminar_tarea())
        self.root.bind("<Delete>", lambda event: self.eliminar_tarea())
        self.root.bind("<Escape>", lambda event: self.root.quit())

    def añadir_tarea(self):
        texto = self.entry_tarea.get().strip()
        if texto:
            self.lista_tareas.insert(tk.END, texto)
            self.entry_tarea.delete(0, tk.END)
        else:
            messagebox.showwarning("Campo vacío", "Por favor escribe una tarea.")

    def marcar_completada(self):
        seleccion = self.lista_tareas.curselection()
        if seleccion:
            index = seleccion[0]
            tarea = self.lista_tareas.get(index)
            if not tarea.startswith("[✔] "):
                self.lista_tareas.delete(index)
                self.lista_tareas.insert(index, "[✔] " + tarea)
        else:
            messagebox.showinfo("Sin selección", "Selecciona una tarea para marcar como completada.")

    def eliminar_tarea(self):
        seleccion = self.lista_tareas.curselection()
        if seleccion:
            index = seleccion[0]
            self.lista_tareas.delete(index)
        else:
            messagebox.showinfo("Sin selección", "Selecciona una tarea para eliminar.")

# Ejecutar la aplicación
if __name__ == "_main_":
    root = tk.Tk()
    app = GestorTareas(root)
    root.mainloop()