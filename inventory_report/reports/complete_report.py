from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    def products_stocked_by_company(list):
        company_name = [name["nome_da_empresa"] for name in list]
        company_count = Counter(company_name).most_common()

        str_report = ""

        for key, value in company_count:
            str_report += f"- {key}: {value}\n"

        return str_report

    @classmethod
    def generate(self, list):
        simple_report = super().generate(list)
        stocked_by_company = self.products_stocked_by_company(list)

        return (
            f"{simple_report}\n"
            f"Produtos estocados por empresa:\n"
            f"{stocked_by_company}"
        )
