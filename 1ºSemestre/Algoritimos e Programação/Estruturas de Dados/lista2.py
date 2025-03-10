temperaturas = [25, 18, 12, 22]
tamanho = len(temperaturas)
soma = 0
for i in temperaturas:
    soma += i
media = soma / tamanho
print(f"Média: {media}")
