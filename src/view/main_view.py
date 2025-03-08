import tkinter as tk
from tkinter import ttk

from src.config import CREATORS
from src.styles import STYLES


class WelcomeView(tk.Frame):
    def __init__(self, root_window, controller=None):
        super().__init__()
        self.controller = controller
        self.root_window = root_window
        self.frame_container = ttk.Frame(self.root_window)
        self.creators = CREATORS
        self.create_widgets()

    def create_widgets(self):
        label_title = self.create_label("Bienvenido al Simulador", 'title')
        label_title.pack(pady=10)

        label_subtitle = self.create_label("Simulador de Números Pseudoaleatorios", 'subtitle')
        label_subtitle.pack(pady=5)

        self.create_creator_label()

        self.btn_simulator = ttk.Button(
            self.frame_container,
            text="Usar Simulador",
            command=self.on_use_simulator
        )
        self.btn_simulator.pack(pady=20)

    def create_creator_label(self):
        label_creator = self.create_label("Creado por:", 'creator_title')
        label_creator.pack(pady=5)
        for creator in self.creators:
            label_creator = self.create_label(creator, 'body')
            label_creator.pack(pady=5)

    def create_label(self, text, style):
        imported_style = STYLES.get(style, {})
        return ttk.Label(self.frame_container, text=text, **imported_style)

    def on_use_simulator(self):
        if self.controller:
            self.controller.show_simulator()

    def destroy(self):
        self.frame_container.destroy()

    def pack(self):
        self.frame_container.pack(fill='both', expand=True, padx=20, pady=20)
