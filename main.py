from banco.banco import Banco
from cliente.cliente import Cliente
from contas.conta_corrente import ContaCorrente
from contas.conta_poupanca import ContaPoupanca

def exibir_menu():
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
    meu_banco = Banco("Banco Tech")
    
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == '0':
            print("Encerrando o sistema. Até logo!")
            break

        elif opcao == '1':
            nome = input("Digite o nome do cliente: ")
            cpf = input("Digite o CPF do cliente: ")
            novo_cliente = Cliente(nome, cpf)

            print("Tipo de Conta: [1] Corrente | [2] Poupança")
            tipo = input("Escolha: ")
            numero = input("Crie um número para a conta: ")

            if tipo == '1':
                nova_conta = ContaCorrente(numero_conta=numero, cliente=novo_cliente)
                meu_banco.adicionar_conta(nova_conta)
            elif tipo == '2':
                nova_conta = ContaPoupanca(numero_conta=numero, cliente=novo_cliente)
                meu_banco.adicionar_conta(nova_conta)
            else:
                print("Tipo inválido!")

        elif opcao == '2':
            numero = input("Digite o número da conta: ")
            conta = meu_banco.buscar_conta(numero)
            
            if conta is not None:
                valor = float(input("Digite o valor do depósito: R$ "))
                conta.depositar(valor)

        elif opcao == '3':
            numero = input("Digite o número da conta: ")
            conta = meu_banco.buscar_conta(numero)
            
            if conta is not None:
                valor = float(input("Digite o valor do saque: R$ "))
                conta.sacar(valor)

        elif opcao == '4':
            numero = input("Digite o número da conta: ")
            conta = meu_banco.buscar_conta(numero)
            
            if conta is not None:
                print(f"Saldo atual: R$ {conta.get_saldo():.2f}")

        elif opcao == '5':
            numero = input("Digite o número da conta: ")
            conta = meu_banco.buscar_conta(numero)
            
            if conta is not None:
                print(f"\n--- Histórico da Conta {conta.numero} ---")
                for operacao in conta.historico.operacoes:
                    print(operacao)
        
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()