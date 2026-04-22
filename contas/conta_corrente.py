from contas.contas import Conta

class ContaCorrente(Conta):
    def __init__(self, numero_conta, cliente, limite=500.0):
        super().__init__(numero_conta, cliente)
        
        self.limite = limite

    def sacar(self, valor):
        if valor > 0 and (self._saldo + self.limite) >= valor:
            self._saldo -= valor
            
            self.historico.adicionar_operacao(f"Saque (CC) de R$ {valor}")
            print(f"Saque de R$ {valor} na Conta Corrente realizado com sucesso!")
            return True
        else:
            print("Operação negada: Saldo e limite insuficientes!")
            return False