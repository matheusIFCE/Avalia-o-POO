# 1. A classe exigida pelo professor
class Operacao:
    def __init__(self, descricao):
        self.descricao = descricao

    # O __str__ ensina o Python como exibir esse objeto no 'print' do main.py
    def __str__(self):
        return self.descricao

# 2. O Histórico que antes estava perdido, agora tem uma casa oficial
class Historico:
    def __init__(self):
        self.operacoes = []

    def adicionar_operacao(self, texto_da_operacao):
        # A MÁGICA: O histórico pega o texto, transforma em um OBJETO Operacao e guarda!
        nova_operacao = Operacao(texto_da_operacao)
        self.operacoes.append(nova_operacao)
