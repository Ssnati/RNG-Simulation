import tkinter as tk
from tkinter import ttk

from src.view.pruebasUI import ChiSquareFrame, MiddleProofFrame, KSFrame

class ventanaPruebas(tk.Tk):
    """
    Clase que representa la ventana principal de pruebas estadísticas.
    Permite al usuario seleccionar y visualizar diferentes pruebas: 
    - Prueba Chi-Cuadrado
    - Prueba de Medias
    - Prueba KS
    """
    def __init__(self, controller):
        """Inicializa la ventana de pruebas."""
        super().__init__()
        self.title("Ventana de Pruebas Estadísticas")
        self.geometry("900x700")
        self.controller = controller  # Controlador para ejecutar las pruebas

        # Frame para los botones de selección
        self.selector_frame = ttk.Frame(self, borderwidth=2, border=10)
        self.selector_frame.pack(fill=tk.X, anchor="sw")

        # Botones para seleccionar pruebas
        ttk.Button(self.selector_frame, text="Prueba Chi-Cuadrado",
                   command=self.show_chi_square).pack(side=tk.LEFT, padx=10, pady=100)
        ttk.Button(self.selector_frame, text="Prueba de Medias",
                   command=self.show_middle_proof).pack(side=tk.LEFT, padx=10)
        ttk.Button(self.selector_frame, text="Prueba KS",
                   command=self.show_ks).pack(side=tk.LEFT, padx=10)

        # Frame contenedor para las pruebas
        self.container_frame = ttk.Frame(self)
        self.container_frame.place(x=20, y=400, anchor="w", width=800, height=500)

        # Inicializar Frames de pruebas (ocultos inicialmente)
        self.chi_square_frame = ChiSquareFrame(self.container_frame)
        self.middle_proof_frame = MiddleProofFrame(self.container_frame)
        self.ks_frame = KSFrame(self.container_frame)

        # Mostrar la primera prueba por defecto
        self.show_chi_square()

        # Iniciar la aplicación
        self.mainloop()

    def show_chi_square(self):
        """Muestra el Frame de la Prueba Chi-Cuadrado y ejecuta la prueba."""
        self.hide_all_frames()
        self.chi_square_frame.pack(fill=tk.BOTH, expand=True)

        # Ejecutar prueba Chi-Cuadrado y actualizar la interfaz con los resultados
        listchi, totals = self.controller.run_test("chi2")  # Devuelve lista de datos y totales
        self.chi_square_frame.fillTable(listchi, totals)

    def show_middle_proof(self):
        """Muestra el Frame de la Prueba de Medias y ejecuta la prueba."""
        self.hide_all_frames()
        self.middle_proof_frame.pack(fill=tk.BOTH, expand=True)

        # Ejecutar prueba de medias y actualizar la interfaz con los resultados
        totals = self.controller.run_test("middleproof")
        self.middle_proof_frame.fillTotals(totals)

    def show_ks(self):
        """Muestra el Frame de la Prueba KS y ejecuta la prueba."""
        self.hide_all_frames()
        self.ks_frame.pack(fill=tk.BOTH, expand=True)

        # Ejecutar prueba KS y actualizar la interfaz con los resultados
        listks, totals = self.controller.run_test("ks")
        self.ks_frame.fillTotals(listks, totals)

    def hide_all_frames(self):
        """Oculta todos los Frames de pruebas para mostrar solo el seleccionado."""
        self.chi_square_frame.pack_forget()
        self.middle_proof_frame.pack_forget()
        self.ks_frame.pack_forget()
