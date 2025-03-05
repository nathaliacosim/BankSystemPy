import textwrap


def menu():
    menu = """\n
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))


def depositar(saldo, valor, extrato):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print("\n=== Depósito realizado com sucesso! Seu saldo foi atualizado. ===")
    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. Tente novamente. @@@")

    return saldo, extrato


def sacar(saldo, valor, extrato, limite, numero_saques, limite_saques):
    if valor <= 0:
        print("\n@@@ Operação falhou! O valor informado é inválido. Tente novamente. @@@")
        return saldo, extrato

    if valor > saldo:
        print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")
    elif valor > limite:
        print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")
    elif numero_saques >= limite_saques:
        print("\n@@@ Operação falhou! Número máximo de saques foi atingido. @@@")
    else:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("\n=== Saque realizado com sucesso! Verifique o seu saldo. ===")

    return saldo, extrato


def exibir_extrato(saldo, extrato):
    print("\n================ EXTRATO ================")
    if not extrato:
        print("Não foram realizadas movimentações. Está tudo tranquilo por aqui!")
    else:
        print(extrato)
    print(f"\nSaldo atual:\tR$ {saldo:.2f}")
    print("==========================================")
    print("\nObrigado por utilizar nosso sistema!")


def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    if filtrar_usuario(cpf, usuarios):
        print("\n@@@ Já existe um usuário com esse CPF! Tente novamente. @@@")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("\n=== Usuário criado com sucesso! Seja bem-vindo! ===")


def filtrar_usuario(cpf, usuarios):
    return next((usuario for usuario in usuarios if usuario["cpf"] == cpf), None)


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! Seu número de conta é: {} ===".format(numero_conta))
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n@@@ Usuário não encontrado! O processo de criação de conta foi interrompido. @@@")
    return None


def listar_contas(contas):
    if not contas:
        print("\n@@@ Não há contas cadastradas ainda. Você pode criar a sua! @@@")
    else:
        for conta in contas:
            linha = f"""\
                Agência:\t{conta['agencia']}
                C/C:\t\t{conta['numero_conta']}
                Titular:\t{conta['usuario']['nome']}
            """
            print("=" * 100)
            print(textwrap.dedent(linha))


def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            try:
                valor = float(input("Informe o valor do depósito: R$ "))
                saldo, extrato = depositar(saldo, valor, extrato)
            except ValueError:
                print("\n@@@ Valor inválido! Informe um número válido. Tente novamente. @@@")

        elif opcao == "s":
            try:
                valor = float(input("Informe o valor do saque: R$ "))
                saldo, extrato = sacar(saldo, valor, extrato, limite, numero_saques, LIMITE_SAQUES)
            except ValueError:
                print("\n@@@ Valor inválido! Informe um número válido. Tente novamente. @@@")

        elif opcao == "e":
            exibir_extrato(saldo, extrato)

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            print("\n=== Sistema encerrado! Até logo e tenha um ótimo dia! ===")
            break

        else:
            print("\n@@@ Operação inválida! Por favor, escolha uma opção válida do menu. @@@")


if __name__ == "__main__":
    main()