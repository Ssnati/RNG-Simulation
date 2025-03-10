import tkinter as tk
from tkinter import ttk

from pruebasUI import ChiSquareFrame, MiddleProofFrame, KSFrame


class ventanaPruebas(tk.Frame):
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Ventana de Pruebas Estadísticas")
        self.root.geometry("1000x800")

        # Frame para los botones de selección
        self.selector_frame = ttk.Frame(self.root, borderwidth=2, border=10)
        self.selector_frame.pack(fill=tk.X, anchor= "sw")

        # Botones para seleccionar pruebas
        ttk.Button(self.selector_frame, text="Prueba Chi-Cuadrado",
                   command=self.show_chi_square).pack(side=tk.LEFT, padx=10, pady=100)
        ttk.Button(self.selector_frame, text="Prueba de Medias",
                   command=self.show_middle_proof).pack(side=tk.LEFT, padx=10)
        ttk.Button(self.selector_frame, text="Prueba KS",
                   command=self.show_ks).pack(side=tk.LEFT, padx=10)

        # Frame contenedor para las pruebas
        self.container_frame = ttk.Frame(self.root)
        self.container_frame.place(x=20, y=400, anchor="w", width=600, height=500)

        # Inicializar Frames de pruebas (ocultos inicialmente)
        self.chi_square_frame = ChiSquareFrame(self.container_frame)
        self.middle_proof_frame = MiddleProofFrame(self.container_frame)
        self.ks_frame = KSFrame(self.container_frame)

        # Mostrar la primera prueba por defecto
        self.show_chi_square()

        # Iniciar la aplicación
        self.root.mainloop()

    def show_chi_square(self):
        """Muestra el Frame de la Prueba Chi-Cuadrado."""
        self.hide_all_frames()
        self.chi_square_frame.pack(fill=tk.BOTH, expand=True)

    def show_middle_proof(self):
        """Muestra el Frame de la Prueba de Medias."""
        self.hide_all_frames()
        self.middle_proof_frame.pack(fill=tk.BOTH, expand=True)

    def show_ks(self):
        """Muestra el Frame de la Prueba KS."""
        self.hide_all_frames()
        self.ks_frame.pack(fill=tk.BOTH, expand=True)

    def hide_all_frames(self):
        """Oculta todos los Frames de pruebas."""
        self.chi_square_frame.pack_forget()
        self.middle_proof_frame.pack_forget()
        self.ks_frame.pack_forget()


if __name__ == "__main__":
    app = ventanaPruebas()
