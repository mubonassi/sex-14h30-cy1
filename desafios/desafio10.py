print("| AUMENTANDO E DIMINUINDO COM ESCOLHA |")
print("-"*20)

valor = float(input("Digite um valor: "))
aumento = int(input("Digite a % de aumento: %"))

valor = valor * (1 + aumento/100)

print(f"Valor com aumento: {valor}")

desconto = int(input("Digite a % do desconto: %"))
valor = valor * (1 - desconto/100)

print(f"Valor final: {valor}")