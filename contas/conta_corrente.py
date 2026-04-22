# 1. IMPORTAÇÃO: "Do pacote 'contas', no módulo 'conta', importe a classe 'Conta'"
from contas.contas import Conta

# 2. HERANÇA: Colocar (Conta) avisa que esta classe é filha da classe base 
class ContaCorrente(Conta):
    def __init__(self, numero_conta, cliente, limite=500.0):
        # 3. O super() chama o __init__ da classe mãe.
        # Ele vai rodar aquele código que você já fez, criando o _saldo e o historico!
        super().__init__(numero_conta, cliente)
        
        # Atributo exclusivo: só a Conta Corrente tem esse limite extra
        self.limite = limite

    # 4. POLIMORFISMO: Reescrevendo o método de saque com uma regra nova 
    def sacar(self, valor):
        # A regra da CC: O valor do saque não pode ultrapassar o (saldo disponível + limite extra)
        if valor > 0 and (self._saldo + self.limite) >= valor:
            self._saldo -= valor
            
            # Registra no histórico que ela herdou da mãe
            self.historico.adicionar_operacao(f"Saque (CC) de R$ {valor}")
            print(f"Saque de R$ {valor} na Conta Corrente realizado com sucesso!")
            return True
        else:
            print("Operação negada: Saldo e limite insuficientes!")
            return False