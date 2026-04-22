# 1. IMPORTAÇÃO: Precisamos puxar a classe base novamente para este arquivo
from contas.contas import Conta

# 2. HERANÇA 
class ContaPoupanca(Conta):
    def __init__(self, numero_conta, cliente):
        # Chama o construtor da mãe. A poupança é simples e não tem atributos extras.
        super().__init__(numero_conta, cliente)

    # 3. POLIMORFISMO: Uma regra de saque mais rígida e totalmente diferente da CC 
    def sacar(self, valor):
        # A regra da Poupança: O valor do saque não pode ser maior que o saldo atual
        if valor > 0 and self._saldo >= valor:
            self._saldo -= valor
            
            self.historico.adicionar_operacao(f"Saque (Poupança) de R$ {valor}")
            print(f"Saque de R$ {valor} na Poupança realizado com sucesso!")
            return True
        else:
            print("Operação negada: Saldo insuficiente na Poupança!")
            return False