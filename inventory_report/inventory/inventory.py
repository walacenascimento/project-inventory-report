import csv
import json
import xml.etree.cElementTree as WN
from ..reports.simple_report import SimpleReport
from ..reports.complete_report import CompleteReport

# Requisito 5, 6 e 7


class Inventory:
    @classmethod
    # Requisito 5
    def import_data(cls, file, type_report):
        lista_produtos = cls.import_file(file)
        if type_report == "simples":
            return SimpleReport.generate(lista_produtos)
        else:
            return CompleteReport.generate(lista_produtos)

    @classmethod
    # Requisito 6
    def import_file(cls, file):
        lista_produtos = []
        if file.endswith("csv"):
            with open(file) as csv_file:
                reader = csv.DictReader(csv_file)
                lista_produtos = [row for row in reader]
            return lista_produtos

        elif file.endswith("json"):
            with open(file) as file_json:
                reader = json.load(file_json)
                lista_produtos = [row for row in reader]
                return lista_produtos
        # Requisto 7
        elif file.endswith("xml"):
            with open(file) as file_xml:
                tree = WN.parse(file_xml)
                root = tree.getroot()
                lista_produtos = [
                    {elem.tag: elem.text for elem in item} for item in root
                ]
            return lista_produtos
