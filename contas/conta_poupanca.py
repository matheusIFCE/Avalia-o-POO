from contas.contas import Conta

class ContaPoupanca(Conta):
    def __init__(self, numero_conta, cliente):
        super().__init__(numero_conta, cliente)

    def sacar(self, valor):
        if valor > 0 and self._saldo >= valor:
            self._saldo -= valor
            
            self.historico.adicionar_operacao(f"Saque (Poupança) de R$ {valor}")
            print(f"Saque de R$ {valor} na Poupança realizado com sucesso!")
            return True
        else:
            print("Operação negada: Saldo insuficiente na Poupança!")
            return False