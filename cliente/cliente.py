class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

    def mostrar_info(self):
        print(f"Cliente: {self.nome} | CPF: {self.cpf}")