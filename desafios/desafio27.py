import random

print("| PERSONALIZADOR DE DADOS |")
print("-"*60)

lados = int(input("Digite a quantidade de lados do [dado]: "))
dado = random.randint(1,lados)

print(f"Você rolou {dado} do [D{lados}]!")

if dado == lados:
    print("VOCÊ **ACERTOU** CRÍTICO!")
elif dado == 1:
    print("VOCÊ >>ERROU<< CRÍTICO!")