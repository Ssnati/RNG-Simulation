import tkinter as tk
from tkinter import ttk


class ChiSquareFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.setup_ui()

    def setup_ui(self):
        """Configura la interfaz de la Prueba Chi-Cuadrado."""
        self.configure(relief=tk.RIDGE, borderwidth=2, padding=10)

        self.create_title()
        self.create_value_labels()
        self.create_table()
        self.create_scrollbar()
        self.create_results()
        self.create_check_label()

    def create_title(self):
        """Crea el título de la prueba."""
        ttk.Label(self, text="Prueba Chi-Cuadrado", font=("Arial", 14)).grid(row=0, column=0, columnspan=2, pady=10)

    def create_value_labels(self):
        """Crea las etiquetas para los valores máximo y mínimo."""
        ttk.Label(self, text="Máximo:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
        self.max_value_label = ttk.Label(self, text="0.0")
        self.max_value_label.grid(row=1, column=0, padx=5, pady=5)

        ttk.Label(self, text="Mínimo:").grid(row=1, column=1, sticky="w", padx=5, pady=5)
        self.min_value_label = ttk.Label(self, text="0.0")
        self.min_value_label.grid(row=1, column=1, padx=5, pady=5)

    def create_table(self):
        """Crea la tabla de intervalos con encabezados."""
        columns = ("No", "Inicial", "Final", "Freq. obten", "Freq. Esperada", "Chi²")
        self.tree = ttk.Treeview(self, columns=columns, show="headings", height=12)

        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=90)

        self.tree.grid(row=3, column=0, columnspan=2, pady=10, sticky="nsew")

    def create_scrollbar(self):
        """Agrega un scrollbar a la tabla."""
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.grid(row=3, column=2, sticky="ns")

    def create_results(self):
        """Crea etiquetas para mostrar los resultados."""
        ttk.Label(self, text="Total suma Chi²:").grid(row=4, column=0, sticky="w", padx=5, pady=5)
        self.chi_square_total_label = ttk.Label(self, text="0.0")
        self.chi_square_total_label.grid(row=4, column=1, sticky="w", padx=5, pady=5)

        ttk.Label(self, text="Prueba gl:").grid(row=5, column=0, sticky="w", padx=5, pady=5)
        self.gl_result_label = ttk.Label(self, text="0")
        self.gl_result_label.grid(row=5, column=1, sticky="w", padx=5, pady=5)

    def create_check_label(self):
        """Muestra si la prueba pasó o no."""
        self.check_label = ttk.Label(self, text="❌ No Sirve", font=("Arial", 12), foreground="red")
        self.check_label.grid(row=6, column=0, columnspan=2, pady=10)


class MiddleProofFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.setup_ui()

    def setup_ui(self):
        """Configura la interfaz de la Prueba de Medias."""
        self.configure(relief=tk.RIDGE, borderwidth=2, padding=10)

        self.create_title()
        self.create_limits_and_average()
        self.create_variance()
        self.create_check_label()

    def create_title(self):
        """Crea el título de la prueba."""
        ttk.Label(self, text="Prueba de Medias", font=("Arial", 14)).pack(pady=10)

    def create_limits_and_average(self):
        """Crea las etiquetas y valores para los límites y el promedio."""
        self.create_label_with_value("Límite Inferior:", "0.0", "inf_lim_label")
        self.create_label_with_value("Promedio:", "0.0", "average_label")
        self.create_label_with_value("Límite Superior:", "0.0", "sup_lim_label")

    def create_variance(self):
        """Crea la etiqueta y valor de la varianza."""
        self.create_label_with_value("Varianza:", "0.0", "variance_label")

    def create_check_label(self):
        """Muestra si la prueba pasó o no."""
        self.check_label = ttk.Label(self, text="❌ No Sirve", font=("Arial", 12), foreground="red")
        self.check_label.pack()

    def create_label_with_value(self, text, value, attribute_name):
        """Crea una etiqueta con su respectivo valor y lo almacena en un atributo."""
        ttk.Label(self, text=text).pack()
        setattr(self, attribute_name, ttk.Label(self, text=value))
        getattr(self, attribute_name).pack()

class KSFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.setup_ui()

    def setup_ui(self):
        """Configura la interfaz de la Prueba KS."""
        self.configure(relief=tk.RIDGE, borderwidth=2, padding=10)

        self.create_labels()
        self.create_table()
        self.create_scrollbar()
        self.create_check_label()

    def create_labels(self):
        """Crea las etiquetas para DM Calculado y DM Crítico."""
        ttk.Label(self, text="Prueba de Kolmogorov-Smirnov", font=("Arial", 14)).grid(row=0, column=0, columnspan=2, pady=10)

        ttk.Label(self, text="DM Calculado:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
        self.dm_calculated_label = ttk.Label(self, text="0.0")
        self.dm_calculated_label.grid(row=1, column=0, padx=5, pady=5)

        ttk.Label(self, text="DM Crítico:").grid(row=2, column=0, sticky="w", padx=5, pady=5)
        self.dm_critic_label = ttk.Label(self, text="0.0")
        self.dm_critic_label.grid(row=2, column=0, padx=5, pady=5)

    def create_table(self):
        """Crea la tabla de intervalos con encabezados."""
        columns = ("Intervalo", "Freq. Obtenida", "Freq. Acumulada", "Prob. Acumulada", "Prob. Esperada", "Diferencia")
        self.tree = ttk.Treeview(self, columns=columns, show="headings", height=15)

        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=90)

        self.tree.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    def create_scrollbar(self):
        """Agrega un scrollbar a la tabla."""
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.grid(row=3, column=2, sticky="ns")

    def create_check_label(self):
        """Muestra si la prueba pasó o no."""
        self.check_label = ttk.Label(self, text="❌ No Sirve", font=("Arial", 12), foreground="red")
        self.check_label.grid(row=4, column=0, columnspan=2, pady=10)