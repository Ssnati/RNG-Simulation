import tkinter as tk
from tkinter import ttk

from src.styles import STYLES


class SimulatorView(tk.Frame):

    def __init__(self, root_window, controller):
        super().__init__()
        self.root_window = root_window
        self.controller = controller
        self.frame_container = ttk.Frame(self.root_window)
        self.create_widgets()

    def create_widgets(self):
        self.create_label("Simulador de Números Pseudoaleatorios", 'title').pack(pady=10)

    def create_label(self, text, style):
        imported_style = STYLES.get(style, {})
        return ttk.Label(self.frame_container, text=text, **imported_style)

    def destroy(self):
        self.frame_container.destroy()

    def pack(self):
        self.frame_container.pack(fill='both', expand=True, padx=20, pady=20)
