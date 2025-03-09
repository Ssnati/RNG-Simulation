import csv


class CsvExporter:
    def __init__(self, path='/'):
        self.path = path

    def export(self, data):
        with open(self.path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)
