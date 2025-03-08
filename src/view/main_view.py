import tkinter as tk
from tkinter import ttk

import src.view.common_creators as cc
from src.config import CREATORS


class WelcomeView(tk.Frame):
    def __init__(self, root_window, controller=None):
        super().__init__()
        self.controller = controller
        self.root_window = root_window
        self.frame_container = ttk.Frame(self.root_window)
        self.creators = CREATORS
        self.create_widgets()

    def create_widgets(self):
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
        label_creator = cc.create_label(self.frame_container, "Creado por:", 'creator_title')
        label_creator.pack(pady=5)
        for creator in self.creators:
            label_creator = cc.create_label(self.frame_container, creator, 'body')
            label_creator.pack(pady=5)

    def on_use_simulator(self):
        if self.controller:
            self.controller.show_simulator()

    def destroy(self):
        self.frame_container.destroy()

    def pack(self):
        self.frame_container.pack(fill='both', expand=True, padx=20, pady=20)
