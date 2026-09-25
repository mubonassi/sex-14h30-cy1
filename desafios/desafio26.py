import random

print("| CARA OU COROA? |")

lados = ["cara","coroa"]
moeda = random.choice(lados)

escolha = input("Escolha 'cara' ou 'coroa': ")

if escolha not in lados:
    print("Você escolheu um lado não existente!")
elif escolha == moeda:
    print(f"Você acertou! Foi {moeda}")
else:
    print(f"Você errou! Foi {moeda}")