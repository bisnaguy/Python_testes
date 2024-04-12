opcao = -1

while opcao != 0:
    opcao = int(input("Escolha uma das opções: \n [1] para sacar \n [2] para exibir o extrato \n [0] para sair \n: *"))

    if opcao == 1:
        print("Saque realizado com sucesso!")
    elif opcao == 2:
        print("Extrato exibido com sucesso!")
    elif opcao == 0:
        print("Operação finalizada")
    else:
        print("opção inválida")