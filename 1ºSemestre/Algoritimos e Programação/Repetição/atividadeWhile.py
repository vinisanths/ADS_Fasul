import math
while True:
    numero = int(input("Digite um número: "))
    if numero == 0:
        break
    quadrado = math.pow(numero, 2)
    raiz = math.sqrt(numero)
    print(f"O quadrado de {numero} é: {quadrado}, e a raiz quadrada é: {raiz:.2f}")
print("Fim do programa")
