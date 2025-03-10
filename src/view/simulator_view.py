import tkinter as tk
from tkinter import ttk, filedialog

import src.view.common_creators as cc
from src.view.generator_and_test_frame import TablesGeneratorAndTestFrame


class SimulatorView(tk.Frame):

    def __init__(self, root_window, controller):
        super().__init__()
        self.root_window = root_window
        self.controller = controller
        self.frame_container = ttk.Frame(self.root_window)
        self.create_widgets()
        self.pack()  # Asegúrate de llamar a pack() aquí

    def create_widgets(self):
        title_label = cc.create_label(self.frame_container, "Simulador de Números Pseudoaleatorios", 'title')
        title_label.grid(row=0, column=0, columnspan=2, rowspan=1)

        # Primero creamos el frame de las tablas (porque le pasaremos su variable al ButtonsFrame)
        self.tables_frame = TablesGeneratorAndTestFrame(self.frame_container, self.controller)
        self.tables_frame.grid(row=3, column=0, columnspan=2)

        # Ahora el frame de botones, pasándole la referencia del tables_frame
        self.buttons_frame = ButtonsFrame(self.frame_container, self.controller, self.tables_frame)
        self.buttons_frame.grid(row=1, column=0, columnspan=2)

        # Espacio de separación entre botones y tabla
        cc.create_label(self.frame_container, " " * 100, 'title').grid(row=2, column=0, columnspan=2, rowspan=1)

    def destroy(self):
        self.frame_container.destroy()

    def pack(self):
        # Le decimos al frame que se expanda y que se llene de acuerdo al tamaño de la ventana
        self.frame_container.grid(row=0, column=0, sticky="nsew")

        # Configuración interna del frame
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)


class ButtonsFrame(tk.Frame):
    def __init__(self, parent, controller, tables_frame):
        super().__init__(parent)
        self.controller = controller
        self.tables_frame = tables_frame  # Referencia al TablesGeneratorAndTestFrame
        self.generator_types = ["LCG", "MLCG", "MiddleSquare", "ProductoMedio", "Exponential"]
        self.generator_test = ["Chi Cuadrada", "Kolmogorov Smirnov", "MiddleProof"]
        self.create_widgets()

    def create_widgets(self):
        # Usamos la variable del generador del tables_frame
        selected_generator = self.tables_frame.generator_var

        # Creamos el combobox en el ButtonsFrame
        generator_combo = ttk.Combobox(self, textvariable=selected_generator, values=self.generator_types, state="readonly")
        generator_combo.grid(row=0, column=0, padx=10, pady=10)

        # Evento cuando seleccionan un item
        def on_select(_):
            selected_value = selected_generator.get()

            # Actualiza los campos de input en tables_frame
            self.tables_frame.update_input_fields()

            # También avisamos al controlador, si se requiere lógica extra
            self.controller.change_generator_selected(selected_value)

        generator_combo.bind("<<ComboboxSelected>>", on_select)

        # Botón para guardar en CSV
        save_button = ttk.Button(
            self,
            text="Guardar en CSV",
            command=self.save,
        )
        save_button.grid(row=0, column=1, padx=10, pady=10)

        # Botón para salir
        exit_button = ttk.Button(
            self,
            text="Salir",
            command=self.controller.exit,
        )
        exit_button.grid(row=0, column=2, padx=10, pady=10)

    def save(self):
        file_path = filedialog.asksaveasfilename(
            parent=self,
            defaultextension=".csv",
            filetypes=[("CSV", "*.csv")]
        )
        if file_path:
            self.controller.save_generation_numbers(file_path)
