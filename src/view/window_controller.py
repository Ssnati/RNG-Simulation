import tkinter as tk
from src.view.main_view import WelcomeView
from src.view.simulator_view import SimulatorView


class WindowMainController(tk.Tk):
    def __init__(self, controller):
        """
        Inicializa la clase WindowMainController con el controlador principal.

        :param controller: El controlador principal de la aplicación.
        """
        super().__init__()
        self.title("Simulador de Números Pseudoaleatorios")
        self.current_view = None
        self.controller = controller

    def show_welcome(self):
        """
        Muestra la vista de bienvenida.
        Destruye la vista actual si existe y crea una nueva instancia de WelcomeView.
        """
        if self.current_view:
            self.current_view.destroy()
        self.current_view = WelcomeView(self, self.controller)
        self.current_view.pack()
        self.center_window()

    def show_simulator(self):
        """
        Muestra la vista del simulador.
        Destruye la vista actual si existe y crea una nueva instancia de SimulatorView.
        """
        if self.current_view:
            self.current_view.destroy()
        self.current_view = SimulatorView(self, self.controller)
        self.current_view.pack()
        self.center_window()

    def center_window(self):
        """
        Centra la ventana principal en la pantalla.
        """
        self.update_idletasks()
        width = self.winfo_reqwidth()
        height = self.winfo_reqheight()
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        self.geometry(f'{width}x{height}+{x}+{y}')

    def start(self):
        """
        Inicia la aplicación mostrando la vista de bienvenida y comenzando el bucle principal de la ventana.
        """
        self.show_welcome()
        self.mainloop()
