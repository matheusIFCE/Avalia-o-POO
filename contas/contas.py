from operacoes.operacoes import Historico

class Conta:
    def __init__(self, numero_conta, cliente):
        self.numero = numero_conta
        self.cliente = cliente
        self._saldo = 0.0 
        
        self.historico = Historico()
        
    def get_saldo(self):
        return self._saldo

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            self.historico.adicionar_operacao(f"Depósito de R$ {valor}")
            print(f"Depósito de R$ {valor} realizado com sucesso!")
        else:
            print("Valor inválido para depósito.")