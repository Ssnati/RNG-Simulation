from tkinter import ttk

from src.styles import STYLES


class SimulatorView:

    def __init__(self, master, controller):
        self.master = master
        self.controller = controller
        self.frame = ttk.Frame(self.master)
        self.create_widgets()

    def create_widgets(self):
        self.frame.pack(fill='both', expand=True, padx=20, pady=20)

        self.create_label("Simulador de Números Pseudoaleatorios", 'title').pack(pady=10)

    def create_label(self, text, style):
        imported_style = STYLES.get(style, {})
        return ttk.Label(self.frame, text=text, **imported_style)

    def destroy(self):
        self.frame.destroy()

    def pack(self):
        self.frame.pack(fill='both', expand=True)
