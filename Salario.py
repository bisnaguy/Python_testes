nome = str(input())
salario = float(input())
vendas = float(input())

receber = salario + (vendas * 0.15)

print(f"TOTAL = R$ {round(receber, 2):.2f}")