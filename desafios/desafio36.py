import random

print("| CARA OU COROA? |")
lados = ["cara","coroa"]


while True:
    moeda = random.choice(lados)

    escolha = input("Escolha 'cara' ou 'coroa' (ou 'sair' para encerrar): ")

    if escolha == "sair":
        break
    elif escolha not in lados:
        print("Você escolheu um lado não existente!")
    elif escolha == moeda:
        print(f"Você acertou! Foi {moeda}")
    else:
        print(f"Você errou! Foi {moeda}")