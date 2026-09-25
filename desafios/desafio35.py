print("| ADIVINHANDO A PALAVRA MÁGICA! |")

palavra = "mágica"
tentativa = ""
erros = 0

while tentativa != palavra:
    tentativa = input("Digite a tentativa (ou 'desistir' para sair): ")
    if tentativa == palavra:
        print("Você acertou!")
        
        if erros == 0:
            print("ERROU NENHUMA!")
        elif erros <= 3:
            print("PARABÉNS! Você errou menos que 3 vezes!")
        else:
            print(f"Você errou: {erros}")
        break
    
    elif tentativa == "desistir":
        print(f"Você desistiu! A palavra era: {palavra}")
        break
    else:
        print("Você errou! Tente novamente!")
        erros += 1