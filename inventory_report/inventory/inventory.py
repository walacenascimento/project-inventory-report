import csv
from ..reports.simple_report import SimpleReport
from ..reports.complete_report import CompleteReport


class Inventory:
    @classmethod
    def import_data(cls, file, type_report):
        lista_produtos = cls.import_file(file)
        if type_report == "simples":
            return SimpleReport.generate(lista_produtos)
        else:
            return CompleteReport.generate(lista_produtos)

    @classmethod
    def import_file(cls, file):
        lista_produtos = []
        with open(file) as csv_file:
            reader = csv.DictReader(csv_file)
            lista_produtos = [row for row in reader]
        return lista_produtos
