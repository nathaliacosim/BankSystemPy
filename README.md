# BankSystemPy 💳🏦

Bem-vindo ao **BankSystemPy**! 🚀

Este é um sistema bancário simples desenvolvido em Python 🐍. Ele permite que o usuário realize operações de **depósito**, **saque**, consulte **extratos**, crie **novas contas** e cadastre **novos usuários**. O sistema é interativo e foi feito para facilitar o gerenciamento de contas bancárias! 💰

## Funcionalidades 💡

- **Depositar**: Adiciona um valor ao saldo da conta 💵.
- **Sacar**: Realiza um saque da conta, com limite de valor e número de saques 🏧.
- **Extrato**: Exibe todas as transações realizadas até o momento, junto com o saldo atual 📑.
- **Cadastro de Novo Usuário**: Cria um novo usuário com CPF, nome, data de nascimento e endereço 🆔.
- **Criação de Conta**: Cria uma nova conta bancária para um usuário já cadastrado 🏦.
- **Listagem de Contas**: Mostra todas as contas bancárias criadas no sistema 📋.

## Requisitos ⚙️

- Python 3.x 🐍

## Como Rodar 🔧

1. Clone o repositório:

   ```bash
   git clone https://github.com/nathaliacosim/BankSystemPy.git
   ```

2. Navegue até a pasta do projeto:

   ```bash
   cd BankSystemPy
   ```

3. Execute os scripts Python:
   ```bash
   python sistema-basico.py
   ```
   ou
   ```bash
   python sistema-funcoes.py
   ```

## Como Funciona 🎯

Ao iniciar o sistema, você será apresentado a um menu com várias opções. O sistema é interativo e apresenta mensagens claras ao longo do fluxo de operações. Você pode realizar as operações conforme sua escolha.

### Exemplos de operações:

- **Depositar**: Para adicionar valores ao seu saldo, basta escolher a opção de depósito e inserir o valor desejado 💸.
- **Sacar**: Se você precisar retirar dinheiro da conta, o sistema verificará se há saldo suficiente, se o valor está dentro do limite de saque e se o número máximo de saques não foi atingido 🔒.
- **Extrato**: O extrato mostra as transações realizadas até o momento, além do saldo final da conta 📊.

## Estrutura do Código 🧩

- **Funções principais**:
  - `menu()`: Exibe o menu de operações 📜.
  - `depositar()`: Realiza depósitos 💵.
  - `sacar()`: Realiza saques com verificações de saldo e limite 💳.
  - `exibir_extrato()`: Exibe o extrato da conta 📑.
  - `criar_usuario()`: Cria um novo usuário 🆔.
  - `criar_conta()`: Cria uma nova conta bancária 🏦.
  - `listar_contas()`: Lista todas as contas criadas 📋.
- **Fluxo**: O sistema é executado em um loop contínuo até que o usuário escolha a opção de sair 🚪. O código é modular, o que facilita futuras melhorias 🔧.

## Contribuindo 🤝

Se você gostaria de melhorar o projeto, sinta-se à vontade para contribuir! Siga estas etapas:

1. Faça um fork deste repositório 🍴.
2. Crie uma branch para a sua feature (`git checkout -b feature/MinhaFeature`).
3. Faça as alterações necessárias e adicione os commits (`git commit -am 'Adiciona nova feature'`).
4. Envie as alterações para o repositório remoto (`git push origin feature/MinhaFeature`).
5. Abra um pull request explicando as mudanças feitas 💬.

## Licença 📜

Este projeto está licenciado sob a MIT License - veja o arquivo [LICENSE](LICENSE) para mais detalhes.
