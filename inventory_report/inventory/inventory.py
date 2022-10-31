import csv
import json
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport
import xmltodict


class Inventory:
    @classmethod
    def read_file(cls, path: str):
        with open(path, encoding="utf-8") as file:
            report = csv.DictReader(file, delimiter=",", quotechar='"')
            if path.endswith(".csv"):
                return list(report)

            elif path.endswith(".json"):
                return json.load(file)

            elif path.endswith(".xml"):
                return xmltodict.parse(file.read())["dataset"]["record"]
            else:
                raise Exception("Arquivo não encontrado")

    @classmethod
    def import_data(cls, path: str, type: str):
        result = cls.read_file(path)
        if type == "simples":
            return SimpleReport.generate(result)
        if type == "completo":
            return CompleteReport.generate(result)
