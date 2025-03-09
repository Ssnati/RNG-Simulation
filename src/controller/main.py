from src.view.window_controller import WindowMainController


class Controller:
    def __init__(self):
        self.controller = WindowMainController(self)
        self.current_generation_method_name = None  # Nombre del método de generación
        self.current_generation_method = None  # Objeto del método de generación
        self.current_generation_list = None  # Lista de números generados

        self.current_test_name = None  # Nombre de la prueba
        self.current_test = None  # Objeto de la prueba
        self.current_test_result = None  # Resultado de la prueba

    def start(self):
        self.controller.start()


if __name__ == '__main__':
    controller = Controller()
    controller.start()
