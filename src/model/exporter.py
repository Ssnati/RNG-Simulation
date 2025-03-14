import csv


class CsvExporter:
    def __init__(self, path='/'):
        """
        Inicializa la clase CsvExporter con la ruta del archivo CSV.

        :param path: Ruta del archivo donde se guardarán los datos.
        """
        self.path = path

    def export(self, data):
        """
        Exporta una lista de datos a un archivo CSV.

        La lista de datos debe estar en el siguiente formato:
        - La lista es una lista de elementos, donde cada elemento puede ser un número o una cadena de texto.
        - Cada elemento de la lista se escribe en una nueva fila del archivo CSV.

        Por ejemplo:
        - Si la lista de datos es [1, 2, 3, 4, 5], el archivo CSV resultante tendrá el siguiente contenido:
          1
          2
          3
          4
          5

        - Si la lista de datos es ["a", "b", "c"], el archivo CSV resultante tendrá el siguiente contenido:
          a
          b
          c

        :param data: Lista de datos a exportar.
        """
        with open(self.path, 'w', newline='') as file:
            writer = csv.writer(file)
            for dat in data:
                writer.writerow([dat])
