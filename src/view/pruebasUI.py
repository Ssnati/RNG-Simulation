import tkinter as tk
from tkinter import ttk

class ChiSquareFrame(ttk.Frame):
    """
    Clase que representa un marco de interfaz gráfica para la prueba de Chi-Cuadrado.
    Contiene etiquetas, tablas y resultados relevantes.
    """
    def __init__(self, parent):
        """Inicializa el marco y configura la interfaz gráfica."""
        super().__init__(parent)
        self.setup_ui()

    def setup_ui(self):
        """Configura la interfaz gráfica del marco."""
        self.configure(relief=tk.RIDGE, borderwidth=2, padding=10)
        self.create_title()
        self.create_value_labels()
        self.create_table()
        self.create_scrollbar()
        self.create_results()

    def create_title(self):
        """Crea el título principal del marco."""
        ttk.Label(self, text="Prueba Chi-Cuadrado", font=("Arial", 14)).grid(row=0, column=0, columnspan=2, pady=10)
 
    def create_value_labels(self):
        """Crea las etiquetas para mostrar valores de máximo y mínimo."""
        ttk.Label(self, text="Máximo:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
        self.max_value_label = ttk.Label(self, text="0.0")
        self.max_value_label.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(self, text="Mínimo:").grid(row=2, column=0, sticky="w", padx=5, pady=5)
        self.min_value_label = ttk.Label(self, text="0.0")
        self.min_value_label.grid(row=2, column=1, padx=5, pady=5)

    def create_table(self):
        """Crea una tabla para mostrar los valores de la prueba Chi-Cuadrado."""
        columns = ("No", "Inicial", "Final", "Freq. obten", "Freq. Esperada", "Chi²")
        self.tree = ttk.Treeview(self, columns=columns, show="headings", height=12)

        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=90)

        self.tree.grid(row=3, column=0, columnspan=2, pady=10, sticky="nsew")

    def create_scrollbar(self):
        """Crea una barra de desplazamiento para la tabla."""
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.grid(row=3, column=2, sticky="ns")

    def create_results(self):
        """Crea las etiquetas para mostrar los resultados finales de la prueba."""
        ttk.Label(self, text="Total suma Chi²:").grid(row=4, column=0, sticky="w", padx=5, pady=5)
        self.chi_square_total_label = ttk.Label(self, text="0.0")
        self.chi_square_total_label.grid(row=4, column=1, sticky="w", padx=5, pady=5)

        ttk.Label(self, text="Gl crítico:").grid(row=5, column=0, sticky="w", padx=5, pady=5)
        self.gl_result_label = ttk.Label(self, text="0")
        self.gl_result_label.grid(row=5, column=1, sticky="w", padx=5, pady=5)

        self.check_label = ttk.Label(self, text="❌ No Sirve", font=("Arial", 12))
        self.check_label.grid(row=6, column=0, columnspan=2, pady=10, sticky="w")

    def update_check_label(self, chi_square_total, gl_critical):
        """Actualiza la etiqueta de validación de la prueba en función del resultado obtenido."""
        if chi_square_total < gl_critical:
            self.check_label.configure(text="✅ La lista de números aleatorios sigue una distribución uniforme", foreground="green")
        else:
            self.check_label.configure(text="❌ La lista de números aleatorios NO sigue una distribución uniforme", foreground="red")

    def fillTable(self, intervals, totals):
        """Llena la tabla con los valores de los intervalos y totales de la prueba Chi-Cuadrado."""
        for row in self.tree.get_children():
            self.tree.delete(row)

        for i, ((min_value, max_value), data) in enumerate(intervals.items(), start=1):
            self.tree.insert("", "end", values=(
                i,
                f"{min_value:.4f}",
                f"{max_value:.4f}",
                data["freq_o"],
                data["freq_e"],
                f"{data['square_chi']:.4f}"
            ))

        self.max_value_label.configure(text=totals["min_value"])
        self.min_value_label.configure(text=totals["max_value"])
        self.chi_square_total_label.configure(text=totals["squ_chi"])
        self.gl_result_label.configure(text=totals["squ_chi_critic"])
        self.update_check_label(totals["squ_chi"], totals["squ_chi_critic"])


class MiddleProofFrame(ttk.Frame):
    """
    Clase que representa un marco de interfaz gráfica para mostrar los resultados de la prueba de medias.
    Incluye etiquetas para mostrar el límite inferior, promedio, límite superior y varianza,
    además de una etiqueta de verificación que indica si la prueba ha sido superada o no.
    """

    def __init__(self, parent):
        """
        Constructor de la clase MiddleProofFrame.
        :param parent: Frame o ventana padre donde se insertará este frame.
        """
        super().__init__(parent)
        self.setup_ui()

    def setup_ui(self):
        """
        Configura la interfaz gráfica del frame, incluyendo su estilo y elementos.
        """
        self.configure(relief=tk.RIDGE, borderwidth=2, padding=10)
        self.create_title()
        self.create_limits_and_average()
        self.create_check_label()

    def create_title(self):
        """
        Crea y posiciona el título de la prueba de medias.
        """
        ttk.Label(self, text="Prueba de Medias", font=("Arial", 14)).pack(pady=10)

    def create_limits_and_average(self):
        """
        Crea y posiciona las etiquetas que mostrarán los valores del límite inferior,
        promedio, límite superior y varianza.
        """
        self.inf_lim_label = ttk.Label(self, text="Límite Inferior: 0.0")
        self.inf_lim_label.pack()
        self.avarage_label = ttk.Label(self, text="Promedio: 0.0")
        self.avarage_label.pack()
        self.sup_lim_label = ttk.Label(self, text="Límite Superior: 0.0")
        self.sup_lim_label.pack()
        self.variance_label = ttk.Label(self, text="Varianza: 0.0")
        self.variance_label.pack()

    def create_check_label(self):
        """
        Crea y posiciona la etiqueta de verificación que indicará si la prueba de medias fue superada.
        """
        self.check_label = ttk.Label(
            self, text="No hay prueba de medias", font=("Arial", 12), foreground="red"
        )
        self.check_label.pack()

    def fillTotals(self, totals):
        """
        Actualiza los valores de las etiquetas con los resultados de la prueba de medias.
        :param totals: Diccionario con los valores de 'inf_lim', 'average', 'sup_lim' y 'variance'.
        """
        self.inf_lim_label.configure(text=f"Límite Inferior: {totals['inf_lim']}")
        self.avarage_label.configure(text=f"Promedio: {totals['average']}")
        self.sup_lim_label.configure(text=f"Límite Superior: {totals['sup_lim']}")
        self.variance_label.configure(text=f"Varianza: {totals['variance']}")

        # Verificación de la prueba de medias
        if totals["inf_lim"] <= totals["average"] <= totals["sup_lim"]:
            self.check_label.configure(
                text="✅ Como el valor promedio se encuentra entre los límites superior e inferior, "
                     "que son los límites de aceptación, se concluye que el método ha pasado la prueba de medias.",
                foreground="green"
            )
        elif totals["inf_lim"] > totals["average"]:
            self.check_label.configure(
                text="❌ Como el valor promedio es menor al límite inferior, el método no ha pasado la prueba de medias.",
                foreground="red"
            )
        elif totals["sup_lim"] < totals["average"]:
            self.check_label.configure(
                text="❌ Como el valor promedio es mayor al límite superior, el método no ha pasado la prueba de medias.",
                foreground="red"
            )
        else:
            self.check_label.configure(
                text="❌ No hay prueba de medias",
                foreground="yellow"
            )
class KSFrame(ttk.Frame):
    """
    Clase que representa la interfaz gráfica para la prueba de Kolmogorov-Smirnov.
    Permite visualizar los resultados de la prueba, incluyendo el cálculo del DM
    y la comparación con el DM crítico.
    """
    def __init__(self, parent):
        """
        Constructor de la clase KSFrame.
        
        :param parent: Widget padre al que pertenece este frame.
        """
        super().__init__(parent)
        self.setup_ui()

    def setup_ui(self):
        """
        Configura la interfaz de usuario del frame.
        """
        self.configure(relief=tk.RIDGE, borderwidth=2, padding=10)
        self.create_labels()
        self.create_table()
        self.create_check_label("")

    def create_labels(self):
        """
        Crea y posiciona las etiquetas de la interfaz gráfica.
        """
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
        """
        Crea y configura la tabla para mostrar los datos de la prueba.
        """
        frame = ttk.Frame(self)
        frame.grid(row=3, column=0, columnspan=3, sticky="nsew", padx=10, pady=10)

        columns = (
            "Inicial", "Final", "Freq. Obtenida", "Freq. Obt Acumulada",
            "Prob. Obt. Acumulada", "Frec. Acum. Esperada",
            "Prob. Esperada Acum", "Diferencia"
        )
        self.tree = ttk.Treeview(frame, columns=columns, show="headings", height=15)

        column_widths = [50, 50, 120, 140, 150, 150, 130, 80]
        for col, width in zip(columns, column_widths):
            self.tree.heading(col, text=col)
            self.tree.column(col, width=width, anchor="center")

        self.tree.pack(side="left", fill="both", expand=True)

        scrollbar = ttk.Scrollbar(frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right", fill="y")

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(3, weight=1)

    def create_check_label(self, message, foreground="black"):
        """
        Crea una etiqueta que muestra el resultado de la prueba de Kolmogorov-Smirnov.
        
        :param message: Mensaje a mostrar en la etiqueta.
        :param foreground: Color del texto de la etiqueta.
        """
        self.check_label = ttk.Label(self, text=message, font=("Arial", 12), foreground=foreground)
        self.check_label.grid(row=4, column=0, columnspan=2, pady=10)

    def fillTotals(self, intervals, totals):
        """
        Llena la tabla con los datos obtenidos y actualiza los resultados de la prueba.
        
        :param intervals: Diccionario con los intervalos y sus respectivos valores.
        :param totals: Diccionario con los valores calculados de DM y DM crítico.
        """
        for row in self.tree.get_children():
            self.tree.delete(row)

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
                "✅ La lista de números aleatorios sigue una distribución uniforme", "green")
        else:
            self.create_check_label(
                "❌ La lista de números aleatorios NO sigue una distribución uniforme", "red")
