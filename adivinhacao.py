j01 = 0
j02 = 11
i = 0

while j01 < 1 or j01 > 10:
    j01 = int(input("Primeiro jogador, escreva um número de 1 até 10: "))

while j02 != j01:
    j02 = int(input("Segundo jogador, escreva um número de 1 até 10: "))
    i += 1
    if j02 < 1 or j02 > 10:
        print("Número inválido: ")
    elif j02 != j01:
        print("Continue tentando!")
    else:
        print()    
        

print(f"Parabéns você acertou o número na sua tentativa {i}")
    