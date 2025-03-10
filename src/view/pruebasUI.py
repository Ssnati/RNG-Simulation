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


    # self.update_check_label()

    def create_title(self):
        """Crea el título de la prueba."""
        ttk.Label(self, text="Prueba Chi-Cuadrado", font=("Arial", 14)
                  ).grid(row=0, column=0, columnspan=2, pady=10)

    def create_value_labels(self):
        """Crea las etiquetas para los valores máximo y mínimo."""
        ttk.Label(self, text="Máximo:").grid(
            row=1, column=0, sticky="w", padx=5, pady=5)
        self.max_value_label = ttk.Label(self, text="0.0")
        self.max_value_label.grid(row=1, column=0, padx=5, pady=5)

        ttk.Label(self, text="Mínimo:").grid(
            row=1, column=1, sticky="w", padx=5, pady=5)
        self.min_value_label = ttk.Label(self, text="0.0")
        self.min_value_label.grid(row=1, column=1, padx=5, pady=5)

    def create_table(self):
        """Crea la tabla de intervalos con encabezados."""
        columns = ("No", "Inicial", "Final",
                   "Freq. obten", "Freq. Esperada", "Chi²")
        self.tree = ttk.Treeview(
            self, columns=columns, show="headings", height=12)

        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=90)

        self.tree.grid(row=3, column=0, columnspan=2, pady=10, sticky="nsew")

    def create_scrollbar(self):
        """Agrega un scrollbar a la tabla."""
        scrollbar = ttk.Scrollbar(
            self, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.grid(row=3, column=2, sticky="ns")

    def create_results(self):
        """Crea etiquetas para mostrar los resultados."""
        ttk.Label(self, text="Total suma Chi²:").grid(
            row=4, column=0, sticky="w", padx=5, pady=5)
        self.chi_square_total_label = ttk.Label(self, text="0.0")
        self.chi_square_total_label.grid(
            row=4, column=1, sticky="w", padx=5, pady=5)

        ttk.Label(self, text="Gl critico:").grid(
            row=5, column=0, sticky="w", padx=5, pady=5)
        self.gl_result_label = ttk.Label(self, text="0")
        self.gl_result_label.grid(row=5, column=1, sticky="w", padx=5, pady=5)

        self.check_label = ttk.Label(self, text="❌ No Sirve", font=("Arial", 12))
        self.check_label.grid(row=6, column=0, columnspan=2, pady=10, sticky="w")

    def update_check_label(self, chi_square_total, gl_critical):
        # Actualiza la etiqueta de verificación según la comparación de Chi² y GL crítico.
        if chi_square_total < gl_critical:
            self.check_label.configure(text="✅ Sirve", foreground="green")
        else:
            self.check_label.configure(text="❌ No Sirve", foreground="red")

    def fillTable(self, intervals, totals):
        # """Llena la tabla con los datos generados en el backend."""
        # Limpia la tabla antes de agregar nuevos datos
        for row in self.tree.get_children():
            self.tree.delete(row)

        # Agrega los datos nuevos
        for i, ((min_value, max_value), data) in enumerate(intervals.items(), start=1):
            self.tree.insert("", "end", values=(
                i,  # Número de intervalo
                f"{min_value:.4f}",  # Límite inferior
                f"{max_value:.4f}",  # Límite superior
                data["freq_o"],  # Frecuencia obtenida
                data["freq_e"],  # Frecuencia esperada
                f"{data['square_chi']:.4f}"  # Diferencia (Chi²)
            ))

        self.max_value_label.configure(text=totals["min_value"])
        self.min_value_label.configure(text=totals["max_value"])
        self.chi_square_total_label.configure(text=totals["squ_chi"])
        self.gl_result_label.configure(text=totals["squ_chi_critic"])
        # {(0, 12): {"freq_o": 0, "freq_e": expected_freq, "square_chi": 0}}
        self.update_check_label(totals["squ_chi"], totals["squ_chi_critic"])


class MiddleProofFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.setup_ui()

    def setup_ui(self):
        """Configura la interfaz de la Prueba de Medias."""
        self.configure(relief=tk.RIDGE, borderwidth=2, padding=10)

        self.create_title()
        self.create_limits_and_average()
        self.create_check_label("")

    def create_title(self):
        """Crea el título de la prueba."""
        ttk.Label(self, text="Prueba de Medias",
                  font=("Arial", 14)).pack(pady=10)

    def create_limits_and_average(self):
        """Crea las etiquetas y valores para los límites y el promedio."""
        self.inf_lim_label = ttk.Label(self, text="Limite Superior: 0.0")
        self.inf_lim_label.pack()
        self.avarage_label = ttk.Label(self, text="Promedio: 0.0")
        self.avarage_label.pack()
        self.sup_lim_label = ttk.Label(self, text="Limite Inferior: 0,0")
        self.sup_lim_label.pack()
        self.variance_label = ttk.Label(self, text="Varianza: 0,0")
        self.variance_label.pack()

    def create_check_label(self, message):
        """Muestra si la prueba pasó o no."""
        self.check_label = ttk.Label(
            self, text=message, font=("Arial", 12), foreground="red")
        self.check_label.pack()

    def fillTotals(self, totals):
        self.inf_lim_label.configure(
            text="Limite Inferior: " + str(totals["inf_lim"]))
        self.avarage_label.configure(
            text="Promedio: " + str(totals["average"]))
        self.sup_lim_label.configure(
            text="Limite Superior: " + str(totals["sup_lim"]))
        self.variance_label.configure(
            text="Varianza: " + str(totals["variance"]))

        if totals["inf_lim"] <= totals["average"] <= totals["sup_lim"]:
            self.create_check_label(
                "Como el valor promedio se encuentra entre los límites superior e inferior,  \n que son los límites de aceptación, se concluye que el método ha pasado la prueba de medias.")
        else:
            self.create_check_label(
                "El método de generación de números aleatorios NO ha pasado la prueba de medias.")


class KSFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.setup_ui()

    def setup_ui(self):
        """Configura la interfaz de la Prueba KS."""
        self.configure(relief=tk.RIDGE, borderwidth=2, padding=10)

        self.create_labels()
        self.create_table()
        self.create_check_label("")

    def create_labels(self):
        """Crea las etiquetas para DM Calculado y DM Crítico."""
        ttk.Label(self, text="Prueba de Kolmogorov-Smirnov", font=("Arial", 14)).grid(
            row=0, column=0, columnspan=2, pady=10
        )

        ttk.Label(self, text="DM Calculado:").grid(
            row=1, column=0, sticky="w", padx=5, pady=5)
        self.dm_calculated_label = ttk.Label(self, text="0.0")
        self.dm_calculated_label.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(self, text="DM Crítico:").grid(
            row=2, column=0, sticky="w", padx=5, pady=5)
        self.dm_critic_label = ttk.Label(self, text="0.0")
        self.dm_critic_label.grid(row=2, column=1, padx=5, pady=5)

    def create_table(self):
        """Crea la tabla de intervalos con encabezados y scrollbar."""
        frame = ttk.Frame(self)
        frame.grid(row=3, column=0, columnspan=3,
                   sticky="nsew", padx=10, pady=10)

        columns = (
            "Inicial", "Final", "Freq. Obtenida", "Freq. Obt Acumulada",
            "Prob. Obt. Acumulada", "Frec. Acum. Esperada",
            "Prob. Esperada Acum", "Diferencia"
        )
        self.tree = ttk.Treeview(
            frame, columns=columns, show="headings", height=15)

        # Ajustar ancho de columnas
        column_widths = [50, 50, 120, 140, 150, 150, 130, 80]
        for col, width in zip(columns, column_widths):
            self.tree.heading(col, text=col)
            self.tree.column(col, width=width, anchor="center")

        self.tree.pack(side="left", fill="both", expand=True)

        # Agregar scrollbar
        scrollbar = ttk.Scrollbar(
            frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right", fill="y")

        # Configurar expansión en el grid
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(3, weight=1)

    def create_check_label(self, message):
        """Muestra si la prueba pasó o no."""
        self.check_label = ttk.Label(
            self, text=message, font=("Arial", 12), foreground="red")
        self.check_label.grid(row=4, column=0, columnspan=2, pady=10)

    def fillTotals(self, intervals, totals):
        """Llena la tabla con los datos generados en el backend."""
        # Limpia la tabla antes de agregar nuevos datos
        for row in self.tree.get_children():
            self.tree.delete(row)

        # Agrega los datos nuevos
        for (inicial, final), data in intervals.items():
            self.tree.insert("", "end", values=(
                f"{inicial:.4f}",  # Límite inferior
                f"{final:.4f}",  # Límite superior
                data["freq_o"],  # Frecuencia obtenida
                data["freq_o_a"],  # Frecuencia obtenida acumulada
                data["prob_o_a"],  # Probabilidad obtenida acumulada
                data["freq_e_a"],  # Frecuencia esperada acumulada
                data["prob_e_a"],  # Probabilidad esperada acumulada
                f"{data['abs_diff']:.4f}"  # Diferencia (KS)
            ))

        self.dm_calculated_label.configure(text=totals["dm_calculated"])
        self.dm_critic_label.configure(text=totals["dm_critic"])

        if totals["dm_critic"] > totals["dm_calculated"]:
            self.create_check_label(
                "La lista de números aleatorios sigue una distribución uniforme")
        else:
            self.create_check_label(
                "La lista de números aleatorios NO sigue una distribución uniforme")

    # Formato KS:
# {(0, 12): {
# "freq_o": 0,
# "freq_e_a": expected_freq * (i + 1),
# "prob_e_a": (expected_freq * (i + 1)) / len(self.number_list),
# "abs_diff": 0}
#             }
