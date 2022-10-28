from inventory_report.inventory.product import Product


def test_cria_produto():
    product = Product(
        1,
        "headphone",
        "TecInova",
        "2021-07-04",
        "2029-02-09",
        "FR48",
        "em caixas"
        )

    assert product.id == 1
    assert product.nome_do_produto == "headphone"
    assert product.nome_da_empresa == "TecInova"
    assert product.data_de_fabricacao == "2021-07-04"
    assert product.data_de_validade == "2029-02-09"
    assert product.numero_de_serie == "FR48"
    assert product.instrucoes_de_armazenamento == "em caixas"
