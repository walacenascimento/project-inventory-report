from inventory_report.inventory.product import Product


def test_relatorio_produto():
    product = Product(
        1,
        "nome_do_produto",
        "nome_da_empresa",
        "26/09/2022",
        "26/09/2025",
        "numero_de_serie",
        "intrucoes_de_armazenamento",
    )
    assert str(product) == (
        f"O produto {product.nome_do_produto} "
        f"fabricado em {product.data_de_fabricacao} "
        f"por {product.nome_da_empresa} "
        f"com validade até {product.data_de_validade} "
        f"precisa ser armazenado {product.instrucoes_de_armazenamento}."
    )
