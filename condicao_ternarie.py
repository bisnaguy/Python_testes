saldo = 500
saque = 3000

status = "Sucesso" if saldo >= saque else "falha"

print(f"{status} ao realizar o saque!")