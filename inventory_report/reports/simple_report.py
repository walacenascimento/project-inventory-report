from datetime import datetime


class SimpleReport:
    @classmethod
    def generate(cls, list_data):
        data_mais_antiga = cls.data_mais_antiga(list_data)
        empresa_com_mais_produto = cls.empresa_com_mais_produto(list_data)
        data_de_validade = cls.data_de_validade(list_data)
        print(
            data_mais_antiga,
            empresa_com_mais_produto,
            data_de_validade,
            "aqui...!!",
        )
        return (
            f"Data de fabricação mais antiga: {data_mais_antiga}\n"
            f"Data de validade mais próxima: {data_de_validade}\n"
            f"Empresa com mais produtos: {empresa_com_mais_produto}"
        )

    @classmethod
    def data_mais_antiga(cls, list_data):
        resultado = [data["data_de_fabricacao"] for data in list_data]
        return min(resultado)

    @classmethod
    def empresa_com_mais_produto(cls, list_data):
        resultado_da_empresa = {}
        nome_da_empresa = [empresa["nome_da_empresa"] for empresa in list_data]
        for empresa in nome_da_empresa:
            if empresa in resultado_da_empresa:
                resultado_da_empresa[empresa] += 1
            else:
                resultado_da_empresa[empresa] = 1
        return max(resultado_da_empresa, key=resultado_da_empresa.get)

    @classmethod
    def data_de_validade(cls, list_data):
        dados = datetime.today().strftime("%Y-%m-%d")
        resultado = []
        for product in list_data:
            if product["data_de_validade"] > dados:
                resultado.append(product["data_de_validade"])
        return min(resultado)
