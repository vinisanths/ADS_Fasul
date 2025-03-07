kwh = int(input("Digite a quantidade de KWh consumida: "))
tipo = input("Digite o tipo de instalação (R para residencial, I para industrial e C para comercial): ")
preco = 0.0
if tipo == "R":
    if kwh <= 500:
        preco = 0.40
    else:
        preco = 0.65
elif tipo == "C":
    if kwh <= 1000:
        preco = 0.55
    else:
        preco = 0.60
elif tipo == "I":
    if kwh <= 5000:
        preco = 0.55
    else:
        preco = 0.60
valor = kwh * preco
print(f"O valor a ser pago é de R${valor:.2f}")
