class Operacao:
    def __init__(self, descricao):
        self.descricao = descricao

    def __str__(self):
        return self.descricao

class Historico:
    def __init__(self):
        self.operacoes = []

    def adicionar_operacao(self, texto_da_operacao):
        nova_operacao = Operacao(texto_da_operacao)
        self.operacoes.append(nova_operacao)
