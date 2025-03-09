from src.model import exporter
from src.view.window_controller import WindowMainController


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


if __name__ == '__main__':
    controller = Controller()
    controller.start()
