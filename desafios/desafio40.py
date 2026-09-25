def rankear(pontos):
    if pontos <= 200:
        print("Você está no ranking: Iniciante")
    elif pontos <= 500:
        print("Você está no ranking: Veterano")
    elif pontos <= 700:
        print("Você está no ranking: Campeão")
    elif pontos <= 1000:
        print("Você está no ranking: Mestre")
    else:
        print("Você está no ranking: Lendário")



print("| RANKING USANDO FUNÇÃO |")
print("-"*60)
print("| RANKING DE JOGO COMBATE DE PIAS |")
print("-"*30)
pontos = int(input("Quantas pias foram destruídas? Digite aqui: "))
rankear(pontos)
