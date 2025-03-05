import tkinter as tk
from tkinter import ttk

from src.config import CREATORS
from src.styles import STYLES


class WelcomeView:

    def __init__(self, controller=None):
        self.controller = controller
        # Esta es la ventana principal de la aplicación
        self.root = tk.Tk()

        self.root.title("Simulador de Números Pseudoaleatorios")
        self.creators = CREATORS
        self.create_widgets()
        self.center_window()

    def create_widgets(self):
        # Este es el panel principal de la ventana, como JPanel en Java
        self.frame = ttk.Frame(self.root, padding=20)
        self.frame.pack(fill='both', expand=True)

        label_title = self.create_label("Bienvenido al Simulador", 'title')
        label_title.pack(pady=10)

        # Subtítulo
        label_subtitle = self.create_label("Simulador de Números Pseudoaleatorios", 'subtitle')
        label_subtitle.pack(pady=5)

        # Información de los creadores
        self.create_creator_label()

        # Botón "Usar Simulador"
        self.btn_simulator = ttk.Button(self.frame, text="Usar Simulador", command=self.on_use_simulator)
        self.btn_simulator.pack(pady=20)

    def center_window(self):
        self.root.update_idletasks()
        width = self.root.winfo_reqwidth()
        height = self.root.winfo_reqheight()
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)

        self.root.geometry(f'{width}x{height}+{int(x)}+{int(y)}')

    def create_creator_label(self):
        label_creator = self.create_label("Creado por:", 'creator_title')
        label_creator.pack(pady=5)
        for creator in self.creators:
            label_creator = self.create_label(creator, 'body')
            label_creator.pack(pady=5)

    def create_label(self, text, style):
        imported_style = STYLES.get(style, {})
        return ttk.Label(self.frame, text=text, **imported_style)

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
