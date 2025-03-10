from src.model import exporter
from src.view.window_controller import WindowMainController

from src.model.random_number import LCG, MLCG, MiddleSquare, ProductoMedio, ExponentialGenerator
from src.model.pruebas import ChiSquare, MiddleProof, KS


class Controller:
    def __init__(self):
        self.main_window = WindowMainController(self)
        self.current_generation_method_name = None  # Nombre del método de generación
        self.current_generation_method = None  # Objeto del método de generación
        self.current_generation_list = []  # Lista de números generados

        self.current_test_name = None  # Nombre de la prueba
        self.current_test = None  # Objeto de la prueba
        self.current_test_result = []  # Resultado de la prueba

        self.exporter = exporter.CsvExporter()

    def save_generation_numbers(self, path):
        self.exporter.path = path
        self.exporter.export(self.current_generation_list)

    def exit(self):
        self.main_window.show_welcome()

    def change_generator_selected(self, selected_generator):
        self.current_generation_method_name = selected_generator

    def show_simulator(self):
        self.main_window.show_simulator()

    def start(self):
        self.main_window.start()

    def generate_numbers(self, generator_name, params):
        """
        Genera números pseudoaleatorios usando el generador seleccionado.
        :param generator_name: Nombre del generador (LCG, MLCG, etc.).
        :param params: Diccionario con los parámetros necesarios para el generador.
        :return: Tupla con (columns, data) para mostrar en la tabla.
        """
        if generator_name == "LCG":
            obj = LCG(params["a"], params["x0"], params["m"], params["c"], params["min_val"], params["max_val"])
            obj.calculate_seed(params["count"])
            columns = ("xi", "ri", "ni")
            data = list(zip(obj.xi_list, obj.ri_list, obj.ni_list))
            self.current_generation_list = obj.ri_list
            # pruebas con ri

        elif generator_name == "MLCG":
            obj = MLCG(params["a"], params["x0"], params["m"], params["min_val"], params["max_val"])
            obj.calculate_seed(params["count"])
            columns = ("xi", "ri", "ni")
            data = list(zip(obj.xi_list, obj.ri_list, obj.ni_list))
            self.current_generation_list = obj.ri_list
            # pruebas con ri

        elif generator_name == "MiddleSquare":
            obj = MiddleSquare(params["number"], params["digits"], count=params["count"])
            columns = ("ni", "ri")
            data = list(zip(obj.list, obj.normalized_list))
            self.current_generation_list = obj.normalized_list
            # pruebas con normalized

        elif generator_name == "ProductoMedio":
            obj = ProductoMedio(params["number1"], params["number2"], params["digits"], count=params["count"])
            columns = ("ni", "ri")
            data = list(zip(obj.list, obj.normalized_list))
            self.current_generation_list = obj.normalized_list
            # pruebas con normalized

        elif generator_name == "Exponential":
            obj = ExponentialGenerator(params["lambda_val"])
            obj.generate(params["count"])
            columns = ("Index", "Value")
            data = list(enumerate(obj.exponential_list, start=1))
            self.current_generation_list = obj.exponential_list
            # pruebas con exponential_list

        else:
            raise ValueError("Generador no reconocido.")

        # Guardar la lista generada en el controlador
        self.current_generation_list = data
        return columns, data

    def run_test(self, test_name):
        """
        Ejecuta la prueba estadística seleccionada.
        :param test_name: Nombre de la prueba a ejecutar.
        :return: Tupla con (columns, data) para mostrar en la tabla.
        """
        if test_name == "chi2":
            self.current_test_name = test_name
            self.current_test = ChiSquare(self.current_generation_list)
            self.current_test.create_intervals()
            self.current_test.calculate_frequence()
            self.current_test.calculate_squ_chi()
            data = {
                "min_value": self.current_test.min_value,
                "max_value": self.current_test.max_value,
                "intervals": self.current_test.intervals,
                "squ_chi": self.current_test.squ_chi,
                "squ_chi_critic": self.current_test.squ_chi_critic,
            }
            self.current_test_result = self.current_test.intervals
            return self.current_test_result, data

        elif test_name == "middleproof":
            self.current_test_name = test_name
            self.current_test = MiddleProof(self.current_generation_list)
            self.current_test.calculate_proof()
            self.current_test_result = {
                "average": self.current_test.average,
                "inf_lim": self.current_test.inf_lim,
                "sup_lim": self.current_test.sup_lim,
                "variance": self.current_test.variance,
            }
            return self.current_test_result

        elif test_name == "ks":
            self.current_test_name = test_name
            self.current_test = KS(self.current_generation_list)
            self.current_test.create_intervals()
            self.current_test.calculate_frequence_obtained()
            self.current_test.calculate_frequence_obtained_acumulated()
            self.current_test.calculate_dm()
            data = {
                "min_value": self.current_test.min_value,
                "max_value": self.current_test.max_value
            }
            self.current_test_result = self.current_test.intervals
            return self.current_test_result, data

        else:
            raise ValueError("Prueba no reconocida.")


if __name__ == '__main__':
    controller = Controller()
    controller.start()
