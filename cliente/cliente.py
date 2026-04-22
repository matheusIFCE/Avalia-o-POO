class Cliente:
    # O __init__ exige que você informe o nome e o CPF para criar um cliente
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

    # Um método extra só para mostrar os dados bonitinhos na tela depois
    def mostrar_info(self):
        print(f"Cliente: {self.nome} | CPF: {self.cpf}")