x = 1
soma = 0
while x <= 4:
    n = int(input(f"Digite o número {x}: "))
    soma += n
    x += 1
media = soma / 4
print(f"Média: {media}")
print("Fim!")