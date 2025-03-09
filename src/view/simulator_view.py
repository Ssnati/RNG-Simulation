import tkinter as tk
from tkinter import ttk, filedialog

import src.view.common_creators as cc


class SimulatorView(tk.Frame):

    def __init__(self, root_window, controller):
        super().__init__()
        self.root_window = root_window
        self.controller = controller
        self.frame_container = ttk.Frame(self.root_window)
        self.create_widgets()

    def create_widgets(self):
        title_label = cc.create_label(self.frame_container, "Simulador de Números Pseudoaleatorios", 'title')
        title_label.grid(row=0, column=0, columnspan=2, rowspan=1)

        self.buttons_frame = ButtonsFrame(self.frame_container, self.controller)
        self.buttons_frame.grid(row=1, column=0, columnspan=2)

        # Este label es para que haya un espacio entre los botones y la tabla
        cc.create_label(self.frame_container, " " * 100, 'title').grid(row=2, column=0, columnspan=2, rowspan=1)

    def destroy(self):
        self.frame_container.destroy()

    def pack(self):
        #  Le decimos al frame que se expanda y que se llene de acuerdo al tamaño de la ventana
        self.frame_container.pack(fill='both', expand=True, padx=20, pady=20)

        # Estos son métodos para la configuración interna del frame por lo que no tiene que ver con la línea anterior
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)


class ButtonsFrame(tk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.generator_types = ["LCG", "Cuadrados Medios", "MLCG", "Exponencial", "Producto Medio"]
        self.generator_test = ["Chi Cuadrada", "Kolmogorov Smirnov", "MiddleProof"]
        self.create_widgets()

    def create_widgets(self):
        selected_generator = tk.StringVar()
        generator_combo = cc.create_combobox(self, self.generator_types, selected_generator, 'combo')
        generator_combo.bind("<<ComboboxSelected>>",
                             lambda _: self.controller.change_generator_selected(selected_generator.get()))
        generator_combo.grid(row=0, column=0, padx=10, pady=10)

        save_button = ttk.Button(
            self,
            text="Guardar en CSV",
            command=self.save,
        )
        save_button.grid(row=0, column=1, padx=10, pady=10)

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
            print(f"Guardando en {file_path}")
            self.controller.save_generation_numbers(file_path)
