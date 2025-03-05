import tkinter as tk
from src.view.main_view import WelcomeView
from src.view.simulator_view import SimulatorView


class WindowMainController(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Simulador de Números Pseudoaleatorios")
        self.current_view = None

    def show_welcome(self):
        if self.current_view:
            self.current_view.destroy()
        self.current_view = WelcomeView(self, self)
        self.current_view.pack()
        self.center_window()

    def show_simulator(self):
        if self.current_view:
            self.current_view.destroy()
        self.current_view = SimulatorView(self, self)
        self.current_view.pack()
        self.center_window()

    def center_window(self):
        self.update_idletasks()
        width = self.winfo_reqwidth()
        height = self.winfo_reqheight()
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        self.geometry(f'{width}x{height}+{x}+{y}')

    def start(self):
        self.show_welcome()
        self.mainloop()
