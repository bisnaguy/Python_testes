conta_normal = True
conta_universitaria = False

saldo = 700
saque = 5000
cheque_especial = 450

if conta_normal:
    if saldo >= saque:
        print("Saque realziado com sucesso!")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com cheque especial!")
    else:
        print("Você não pode sacar!")
elif conta_universitaria:
    if saque <= saldo:
        print("Saque realizado com sucesso!")
    else:
        print("Você não pode sacar!")        