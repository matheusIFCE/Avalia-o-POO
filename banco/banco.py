class Banco:
    def __init__(self, nome_do_banco):
        self.nome = nome_do_banco
        
        # O banco nasce com um "fichário" (lista) vazio para guardar as contas
        self.contas_cadastradas = []

    # AGREGAÇÃO: O banco RECEBE uma conta que já foi criada em outro lugar
    def adicionar_conta(self, conta_pronta):
        self.contas_cadastradas.append(conta_pronta)
        print(f"Conta número {conta_pronta.numero} adicionada ao banco {self.nome}!")

    # Método para o banco procurar uma conta no fichário
    def buscar_conta(self, numero_da_conta):
        for conta in self.contas_cadastradas:
            if conta.numero == numero_da_conta:
                return conta
        
        print("Conta não encontrada no sistema.")
        return None