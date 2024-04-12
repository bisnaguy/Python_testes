# nome = str(input())
# salario = float(input())
# vendas = float(input())

# receber = salario + (vendas * 0.15)

# print(f"TOTAL = R$ {receber:.2f}")
nome_vendedor=str(input())
salario_fixo= float(input())
total_vendas= float(input())

salario_final= salario_fixo + (total_vendas * 0.15)

print("TOTAL = R$ ", salario_final)