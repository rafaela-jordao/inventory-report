from collections import Counter
from datetime import datetime


class SimpleReport:
    @classmethod
    def fabrication_date(self, list):
        fabrication = [item["data_de_fabricacao"] for item in list]
        return min(fabrication)

    @classmethod
    def validad_date(self, list):
        validad = [
            item["data_de_validade"]
            for item in list
            if item["data_de_validade"] > str(datetime.today().date())
        ]
        return min(validad)

    @classmethod
    def get_max_products(self, list):
        result = [item["nome_da_empresa"] for item in list]
        counter = Counter(result)
        return max(counter, key=counter.get)

    @classmethod
    def generate(self, list):
        fab = self.fabrication_date(list)
        venc = self.validad_date(list)
        name = self.get_max_products(list)

        return (
            f"Data de fabricação mais antiga: {fab}\n"
            f"Data de validade mais próxima: {venc}\n"
            f"Empresa com mais produtos: {name}"
        )
