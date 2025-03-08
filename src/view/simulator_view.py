import tkinter as tk
from tkinter import ttk

import src.view.common_creators as cc


class SimulatorView(tk.Frame):

    def __init__(self, root_window, controller):
        super().__init__()
        self.root_window = root_window
        self.controller = controller
        self.frame_container = ttk.Frame(self.root_window)
        self.create_widgets()

    def create_widgets(self):
        cc.create_label(self.frame_container, "Simulador de Números Pseudoaleatorios", 'title').pack(pady=10)

    def destroy(self):
        self.frame_container.destroy()

    def pack(self):
        self.frame_container.pack(fill='both', expand=True, padx=20, pady=20)
