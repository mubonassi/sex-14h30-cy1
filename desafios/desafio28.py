import random

print("| JO-KEN-POH! (Player vs CPU)|")

formas = ["pedra","papel","tesoura"]
cpu = random.choice(formas)
player = input(">> Escolha 'pedra', 'papel' ou 'tesoura': ").lower()

print(">> PLAYER vs CPU <<")
print(f">> {player} vs {cpu} <<")

if player not in formas:
    print("Você não escolheu um válido! Você perdeu por padrão!")
elif player == cpu:
    print("Empate!")
elif player == "pedra":
    if cpu == "papel":
        print("Você perdeu!")
    else:
        print("Você ganhou!")
elif player == "papel":
    if cpu == "tesoura":
        print("Você perdeu!")
    else:
        print("Você ganhou!")
elif player == "tesoura":
    if cpu == "pedra":
        print("Você perdeu!")
    else:
        print("Você ganhou!")