from src.model import exporter
from src.view.window_controller import WindowMainController

from src.model.random_number import LCG, MLCG, MiddleSquare, ProductoMedio, ExponentialGenerator

class Controller:
    def __init__(self):
        self.controller = WindowMainController(self)
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
        print(self.current_generation_list)

    def exit(self):
        self.controller.show_welcome()

    def change_generator_selected(self, selected_generator):
        self.current_generation_method_name = selected_generator
        print(selected_generator)

    def show_simulator(self):
        self.controller.show_simulator()

    def start(self):
        self.controller.start()

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

        elif generator_name == "MLCG":
            obj = MLCG(params["a"], params["x0"], params["m"], params["min_val"], params["max_val"])
            obj.calculate_seed(params["count"])
            columns = ("xi", "ri", "ni")
            data = list(zip(obj.xi_list, obj.ri_list, obj.ni_list))

        elif generator_name == "MiddleSquare":
            obj = MiddleSquare(params["number"], params["digits"], count=params["count"])
            columns = ("xi", "ri")
            data = list(zip(obj.values, obj.normalized_values))

        elif generator_name == "ProductoMedio":
            obj = ProductoMedio(params["number1"], params["number2"], params["digits"], count=params["count"])
            columns = ("xi", "ri")
            data = list(zip(obj.list, obj.normalized_list))

        elif generator_name == "Exponential":
            obj = ExponentialGenerator(params["lambda_val"])
            obj.generate(params["count"])
            columns = ("Index", "Value")
            data = list(enumerate(obj.exponential_list, start=1))

        else:
            raise ValueError("Generador no reconocido.")

        # Guardar la lista generada en el controlador
        self.current_generation_list = data
        return columns, data
    def __init__(self):
        self.controller = WindowMainController(self)
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
        print(self.current_generation_list)

    def exit(self):
        self.controller.show_welcome()

    def change_generator_selected(self, selected_generator):
        self.current_generation_method_name = selected_generator
        print(selected_generator)


    def show_simulator(self):
        self.controller.show_simulator()

    def start(self):
        self.controller.start()


if __name__ == '__main__':
    controller = Controller()
    controller.start()
