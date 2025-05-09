import tkinter as tk
from tkinter import ttk, messagebox


class TablesGeneratorAndTestFrame(tk.Frame):
    def __init__(self, parent, controller=None):
        super().__init__(parent)
        self.controller = controller
        self.parent = parent

        # Contenedor general que divide en izquierda y derecha
        self.main_container = tk.Frame(self)
        self.main_container.pack(fill=tk.BOTH, expand=True)

        # Frame izquierdo para la tabla
        self.left_frame = tk.Frame(self.main_container)
        self.left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Frame derecho para los inputs y botones
        self.right_frame = tk.Frame(self.main_container)
        self.right_frame.pack(side=tk.RIGHT, fill=tk.Y, padx=10, pady=10)

        # Título del frame (lo ponemos arriba en el frame derecho)
        tk.Label(self.right_frame, text="Generadores de Números Pseudoaleatorios", font=("Arial", 16)).pack(pady=10)

        # Variable para almacenar el generador seleccionado
        self.generator_var = tk.StringVar(value="LCG")

        # Sección de Inputs
        self.input_frame = tk.Frame(self.right_frame)
        self.input_frame.pack(pady=10)

        # Sección de Botones
        self.generate_button = tk.Button(self.right_frame, text="Generar Números", command=self.generate_numbers)
        self.generate_button.pack(pady=5)

        # Sección de Resultados (Tabla)
        self.result_frame = tk.Frame(self.left_frame)
        self.result_frame.pack(fill=tk.BOTH, expand=True)

        self.test_button = tk.Button(self.left_frame, text="Hacer Pruebas", command=self.controller.show_test_window)
        self.test_button.pack(pady=5)

        self.tree = None

        # Inicializa los campos de entrada según el generador inicial
        self.update_input_fields()

    def clear_input_frame(self):
        for widget in self.input_frame.winfo_children():
            widget.destroy()

    def clear_result_frame(self):
        if self.tree:
            self.tree.destroy()
            self.tree = None

    def update_input_fields(self, event=None):
        self.clear_input_frame()

        generator = self.generator_var.get()

        # Diccionario para almacenar las entradas
        self.entries = {}

        # Define los campos según el generador seleccionado
        params = []
        if generator == "LCG":
            params = ["a", "x0", "m", "c", "min_val", "max_val", "count"]
        elif generator == "MLCG":
            params = ["a", "x0", "m", "min_val", "max_val", "count"]
        elif generator == "MiddleSquare":
            params = ["number", "digits", "count"]
        elif generator == "ProductoMedio":
            params = ["number1", "number2", "digits", "count"]
        elif generator == "Exponential":
            params = ["lambda_val", "count"]

        for param in params:
            label = tk.Label(self.input_frame, text=param + ":")
            label.pack(anchor=tk.W)
            entry = tk.Entry(self.input_frame)
            entry.pack(fill=tk.X)
            self.entries[param] = entry

    def generate_numbers(self):
        generator = self.generator_var.get()

        # Intenta convertir las entradas a los tipos adecuados
        try:
            params = {k: float(v.get()) if "." in v.get() else int(v.get()) for k, v in self.entries.items()}
        except ValueError:
            messagebox.showerror("Error de entrada", "Por favor, introduce valores numéricos válidos.")
            return

        self.clear_result_frame()

        # Llama al controlador para generar los números
        try:
            columns, data = self.controller.generate_numbers(generator, params)
            self.display_table(columns, data)
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def display_table(self, columns, data):
        # Crea un Treeview para mostrar los datos
        self.tree = ttk.Treeview(self.result_frame, columns=columns, show='headings')

        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, anchor=tk.CENTER, width=100)

        for row in data:
            self.tree.insert('', tk.END, values=row)

        self.tree.pack(fill=tk.BOTH, expand=True)
