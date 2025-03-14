import tkinter as tk
from tkinter import ttk

import src.view.common_creators as cc
from src.config import CREATORS


class WelcomeView(tk.Frame):
    def __init__(self, root_window, controller=None):
        """
        Inicializa la clase WelcomeView con la ventana raíz y el controlador opcional.

        :param root_window: La ventana raíz de la aplicación.
        :param controller: El controlador opcional para manejar eventos.
        """
        super().__init__()
        self.controller = controller
        self.root_window = root_window
        self.frame_container = ttk.Frame(self.root_window)
        self.creators = CREATORS
        self.create_widgets()

    def create_widgets(self):
        """
        Crea y organiza los widgets en la vista de bienvenida.
        """
        label_title = cc.create_label(self.frame_container, "Bienvenido al Simulador", 'title')
        label_title.pack(pady=10)

        label_subtitle = cc.create_label(self.frame_container, "Simulador de Números Pseudoaleatorios", 'subtitle')
        label_subtitle.pack(pady=5)

        self.create_creator_label()

        self.btn_simulator = ttk.Button(
            self.frame_container,
            text="Usar Simulador",
            command=self.on_use_simulator
        )
        self.btn_simulator.pack(pady=20)

    def create_creator_label(self):
        """
        Crea y organiza las etiquetas de los creadores en la vista de bienvenida.
        """
        label_creator = cc.create_label(self.frame_container, "Creado por:", 'creator_title')
        label_creator.pack(pady=5)
        for creator in self.creators:
            label_creator = cc.create_label(self.frame_container, creator, 'body')
            label_creator.pack(pady=5)

    def on_use_simulator(self):
        """
        Maneja el evento de clic en el botón "Usar Simulador".
        Llama al método del controlador para mostrar el simulador.
        """
        if self.controller:
            self.controller.show_simulator()

    def destroy(self):
        """
        Destruye el contenedor del frame.
        """
        self.frame_container.destroy()

    def pack(self):
        """
        Empaqueta el contenedor del frame con relleno y expansión.
        """
        self.frame_container.pack(fill='both', expand=True, padx=20, pady=20)
