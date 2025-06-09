usuarios = {}

nome = input("Seu nome: ")
senha = input("Sua senha: ")
cadastro = [nome, senha]

usuarios[nome] = {
    "senha": senha,
    "tipo": "",
    "saldo": 0.0,
    "extrato": [],
    "transacoes_dia": 0
}

limitexmoney = 500.00
limitexday = 3

# Escolher tipo de conta
while True:
    tipo = input("Digite seu tipo de conta (a = all, c = corrente, p = poupança): ").lower()
    if tipo in ["a", "c", "p"]:
        usuarios[nome]["tipo"] = tipo
        print(f"Conta criada como tipo '{tipo}'")
        break
    else:
        print("Tipo inválido. Tente novamente.")

# Menu principal
while True:
    print("\n==== MENU ====")
    print("d - Depositar")
    print("s - Sacar")
    print("v - Ver saldo")
    print("e - Ver extrato")
    print("x - Sair")

    op = input("Escolha uma opção: ").lower()

    if op == "d":
        valor = float(input("Valor do depósito: R$ "))
        if valor > 0:
            usuarios[nome]["saldo"] += valor
            usuarios[nome]["extrato"].append(f"Depósito: R$ {valor:.2f}")
            print(f"Depósito realizado! Novo saldo: R$ {usuarios[nome]['saldo']:.2f}")
        else:
            print("Valor inválido para depósito.")

    elif op == "s":
        if usuarios[nome]["transacoes_dia"] >= limitexday:
            print("Limite diário de saques atingido.")
            continue
        valor = float(input("Valor do saque: R$ "))
        if valor > usuarios[nome]["saldo"]:
            print("Saldo insuficiente.")
        elif valor > limitexmoney:
            print("Valor excede o limite de R$ 500.00 por saque.")
        elif valor <= 0:
            print("Valor inválido.")
        else:
            usuarios[nome]["saldo"] -= valor
            usuarios[nome]["transacoes_dia"] += 1
            usuarios[nome]["extrato"].append(f"Saque: R$ {valor:.2f}")
            print(f"Saque realizado! Novo saldo: R$ {usuarios[nome]['saldo']:.2f}")

    elif op == "v":
        print(f"Saldo atual: R$ {usuarios[nome]['saldo']:.2f}")

    elif op == "e":
        print("\nExtrato:")
        if not usuarios[nome]["extrato"]:
            print("Nenhuma movimentação registrada.")
        else:
            for item in usuarios[nome]["extrato"]:
                print(item)
        print(f"Saldo atual: R$ {usuarios[nome]['saldo']:.2f}")

    elif op == "x":
        print("Saindo... Obrigado por usar nosso sistema.")
        break

    else:
        print("Opção inválida.")


