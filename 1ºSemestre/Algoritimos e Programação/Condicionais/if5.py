#Faixa Etária

idade = int(input("Digite a idade: "))
if idade > 18:
    print("Adulto")
elif idade >= 12:
    print("Adolescente")
else:
    print("Criança")
print("Fim do programa.")