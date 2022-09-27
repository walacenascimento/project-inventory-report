from .simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, list_data):
        dados = {}
        nome_da_empresa = [empresa['nome_da_empresa'] for empresa in list_data]
        for empresa in nome_da_empresa:
            if empresa in dados:
                dados[empresa] += 1
            else:
                dados[empresa] = 1

        resultado = dados.items()
        resultfinal = ""
        for name, qnty in resultado:
            resultfinal += (f"- {name}: {qnty}\n")
        print(nome_da_empresa, 'companies_result completeReport  aqui')
        print(resultado, 'result completeReport  aqui  !!!!!!')
        return (
            f"{SimpleReport.generate(list_data)}\n"
            f"Produtos estocados por empresa:\n"
            f"{resultfinal}")
