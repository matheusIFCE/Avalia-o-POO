# 1. IMPORTAÇÕES: Trazendo as classes que criamos nas outras pastas
from banco.banco import Banco
from cliente.cliente import Cliente
from contas.conta_corrente import ContaCorrente
from contas.conta_poupanca import ContaPoupanca

def exibir_menu():
    # Interface baseada nas exigências do professor
    print("\n" + "="*30)
    print("=== CAIXA ELETRÔNICO ===")
    print("1 - Criar Conta")
    print("2 - Depositar")
    print("3 - Sacar")
    print("4 - Consultar Saldo")
    print("5 - Histórico")
    print("0 - Sair")
    print("="*30)

def main():
    # Instanciando o nosso Banco para guardar as contas (Agregação)
    meu_banco = Banco("Banco Tech")
    
    # O 'while True' cria um loop infinito. O menu vai ficar aparecendo
    # até o usuário digitar '0' e acionar o comando 'break'.
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        # OPÇÃO 0: SAIR
        if opcao == '0':
            print("Encerrando o sistema. Até logo!")
            break  # Corta o loop e finaliza o programa

        # OPÇÃO 1: CRIAR CONTA
        elif opcao == '1':
            nome = input("Digite o nome do cliente: ")
            cpf = input("Digite o CPF do cliente: ")
            # Criamos o objeto Cliente
            novo_cliente = Cliente(nome, cpf)

            print("Tipo de Conta: [1] Corrente | [2] Poupança")
            tipo = input("Escolha: ")
            numero = input("Crie um número para a conta: ")

            if tipo == '1':
                # Criamos uma Conta Corrente e passamos o cliente para dentro dela
                nova_conta = ContaCorrente(numero_conta=numero, cliente=novo_cliente)
                meu_banco.adicionar_conta(nova_conta)
            elif tipo == '2':
                # Criamos uma Conta Poupança
                nova_conta = ContaPoupanca(numero_conta=numero, cliente=novo_cliente)
                meu_banco.adicionar_conta(nova_conta)
            else:
                print("Tipo inválido!")

        # OPÇÃO 2: DEPOSITAR
        elif opcao == '2':
            numero = input("Digite o número da conta: ")
            # Usamos o método do banco para achar a conta na lista
            conta = meu_banco.buscar_conta(numero)
            
            if conta is not None:
                # input() recebe texto. float() transforma esse texto em número decimal
                valor = float(input("Digite o valor do depósito: R$ "))
                conta.depositar(valor)

        # OPÇÃO 3: SACAR
        elif opcao == '3':
            numero = input("Digite o número da conta: ")
            conta = meu_banco.buscar_conta(numero)
            
            if conta is not None:
                valor = float(input("Digite o valor do saque: R$ "))
                # Aqui o Polimorfismo age! O Python sabe automaticamente
                # se vai usar a regra da CC ou da Poupança.
                conta.sacar(valor)

        # OPÇÃO 4: CONSULTAR SALDO
        elif opcao == '4':
            numero = input("Digite o número da conta: ")
            conta = meu_banco.buscar_conta(numero)
            
            if conta is not None:
                # O encapsulamento em ação: usando o getter para ver o saldo
                print(f"Saldo atual: R$ {conta.get_saldo():.2f}")

        # OPÇÃO 5: HISTÓRICO
        elif opcao == '5':
            numero = input("Digite o número da conta: ")
            conta = meu_banco.buscar_conta(numero)
            
            if conta is not None:
                print(f"\n--- Histórico da Conta {conta.numero} ---")
                # Acessando a lista de operações que está dentro do objeto Histórico (Composição)
                for operacao in conta.historico.operacoes:
                    print(operacao)
        
        else:
            print("Opção inválida. Tente novamente.")

# Essa linha serve para rodar o programa quando você der 'play' neste arquivo
if __name__ == "__main__":
    main()