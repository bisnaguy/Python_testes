nome = str(input("Informe o nome do vendedor: "))
salario = float(input("Informe o salário do vendedor: "))
vendas = float(input("Informe a quantidade de vendas desse vendedor: "))

receber = salario + (vendas * 0.15)

print(f"O vendedor {nome} tem o salário fixo de  {salario:.2f} junto a comissão de 15% sobre {vendas:.2f} acabou por receber o total de {round(receber, 2):.2f}")