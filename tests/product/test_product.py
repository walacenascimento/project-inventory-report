from inventory_report.inventory.product import Product


def test_cria_produto():
    product = Product(
        1,
        "nome_do_produto",
        "nome_da_empresa",
        "26/09/2022",
        "26/09/2025",
        "numero_de_serie",
        "intrucoes_de_armazenamento",
    )
    assert product.id == 1
    assert product.nome_do_produto == "nome_do_produto"
    assert product.data_de_fabricacao == "26/09/2022"
    assert product.data_de_validade == "26/09/2025"
    assert product.instrucoes_de_armazenamento == "intrucoes_de_armazenamento"
