**Sistema de Caixa Eletrônico - POO em Python**

Esse projeto é um simulador de Caixa Eletrônico feito em Python para colocar em prática os conceitos de Programação Orientada a Objetos.

**Organização das Pastas**
Para deixar o código mais organizado e com um rendimento melhor, o sistema foi dividido em pacotes (pastas). Cada parte do sistema tem o seu lugar:
* banco: cuida do sistema geral e guarda as contas cadastradas.
* clientes: guarda as informações básicas dos titulares.
* operacoes: registra as transações no histórico do cliente.

**Relação entre as Contas**
A parte das contas foi dividida em arquivos diferentes para mostrar o uso de herança na prática:
* Classe Conta: é a classe mãe. Ela tem a estrutura base e protege o saldo.
* Classes ContaCorrente e ContaPoupanca: são as classes filhas. Elas herdam as informações da conta mãe, mas cada uma tem a sua própria regra diferente na hora de sacar o dinheiro.

**A interface principal**
O arquivo main.py é só a tela do sistema. Ele mostra o menu interativo e recebe as opções que o usuário digita. Ele não faz cálculos matemáticos, apenas repassa as tarefas para as classes certas fazerem o trabalho.

**Como rodar o projeto:**
1. Abra o terminal na pasta principal do projeto.
2. Digite o comando: python main.py