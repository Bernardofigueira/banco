saldo = [0]  # Agora o saldo está dentro de uma lista
nome = input('Digite o nome do titular da conta: ')
titular = (nome,)

deposito = float(input("Digite o valor do depósito inicial: R$ "))
if deposito < 0:
    print('Insira um valor positivo!!')
else:
    saldo[0] += deposito

historico = [f"Depósito inicial: R$ {deposito:.2f}"]

while True:
    print("1 - Depositar")
    print("2 - Sacar")
    print("3 - Consultar Saldo")
    print("4 - Consultar Histórico")
    print("5 - Sair")

    acao = input('Escolha uma opção: ')

    if acao == "1":
        valor_deposito = float(input("Digite o valor a ser depositado: R$ "))
        if valor_deposito > 0:
            saldo[0] += valor_deposito
            historico.append(f"Depósito: R$ {valor_deposito:.2f}")
        else:
            print("Valor inválido. Tente novamente.")

    elif acao == "2":
        sacar = float(input("Digite o valor a ser sacado: R$ "))
        if sacar > 0:
            if sacar <= saldo[0]:
                saldo[0] -= sacar
                historico.append(f"Saque: R$ {sacar:.2f}")
            else:
                print('Saldo Insuficiente')
        else:
            print('Insira um valor positivo')

    elif acao == "3":
        print("Saldo atual: R$ {:.2f}".format(saldo[0]))
    elif acao == "4":
        print("Histórico de operações:")
        for item in historico:
            print("-", item)
    elif acao == "5":
        print('Obrigado por contar conosco!')
        break  # ou use exit()
    else:
        print("Opção inválida. Tente novamente.")
