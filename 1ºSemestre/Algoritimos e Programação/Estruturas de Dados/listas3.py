temperaturas = []
while True:
    t = int(input("Digite uma temperatura ou 0 para sair: "))
    if t == 0:
        break
    temperaturas.append(t)
tamanho = len(temperaturas)
soma = 0
for i in temperaturas:
    soma += i
media = soma / tamanho
print(f"Temperaturas: {temperaturas}")
print(f"Média: {media}")