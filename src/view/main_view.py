import tkinter as tk
from tkinter import ttk

from src.config import CREATORS


class WelcomeView:

    def __init__(self, controller=None):
        self.controller = controller
        self.root = tk.Tk()
        self.root.title("Simulador de Números Pseudoaleatorios")
        self.creators = CREATORS
        self.create_widgets()
        self.center_window()

    def center_window(self):
        self.root.update_idletasks()
        width = self.root.winfo_reqwidth()
        height = self.root.winfo_reqheight()
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)

        self.root.geometry(f'{width}x{height}+{int(x)}+{int(y)}')

    def create_widgets(self):
        self.frame = ttk.Frame(self.root, padding=20)
        self.frame.pack(fill='both', expand=True)

        self.label_title = ttk.Label(self.frame, text="Bienvenido al Simulador", font=("Helvetica", 16))
        self.label_title.pack(pady=10)

        # Subtítulo
        self.label_subtitle = ttk.Label(self.frame, text="Simulador de Números Pseudoaleatorios",
                                        font=("Helvetica", 12))
        self.label_subtitle.pack(pady=5)

        # Información de los creadores
        self.create_creator_label()

        # Botón "Usar Simulador"
        self.btn_simulator = ttk.Button(self.frame, text="Usar Simulador", command=self.on_use_simulator)
        self.btn_simulator.pack(pady=20)

    def create_creator_label(self):
        ttk.Label(self.frame, text="Creado por:", font=("Helvetica", 12)).pack(pady=5)
        for creator in self.creators:
            ttk.Label(self.frame, text=creator, font=("Helvetica", 10)).pack(pady=2)

    def on_use_simulator(self):
        # Acción al pulsar el botón: aquí se podría cambiar a la vista del simulador
        print("Botón 'Usar Simulador' presionado")
        if self.controller:
            self.controller.open_simulator()  # Llamada a método del controlador
        else:
            # Por ahora, cerramos la ventana para demostrar la funcionalidad
            self.root.destroy()

    def start(self):
        self.root.mainloop()
