print("| ADIVINHANDO A PALAVRA MÁGICA |")
print("-"*30)

palavraMagica = "lasanha"

tentativa = input("Digite a sua tentativa de palavra: ")

if tentativa == palavraMagica:
    print("Você acertou a palavra mágica!")
else:
    print("Você errou a palavra mágica!")