def funcao1():
    print("| OPERADORES DIFERENTES |")

    numero1 = int(input("Digite o Número #1: "))
    numero2 = int(input("Digite o Número #2: "))

    soma = numero1+numero2
    sub = numero1-numero2
    div = numero1/numero2
    mult = numero1*numero2
    pot = numero1**numero2

    print(f"{numero1} + {numero2} = {soma}")
    print(f"{numero1} - {numero2} = {sub}")
    print(f"{numero1} / {numero2} = {div}")
    print(f"{numero1} * {numero2} = {mult}")
    print(f"{numero1} ^ {numero2} = {pot}")

def funcao2():
    print("| RANKING DE JOGO COMBATE DE PIAS |")
    print("-"*30)

    pontos = int(input("Quantas pias foram destruídas? Digite aqui: "))

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

def funcao3():
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

print("| CAIXA DE FERRAMENTAS |")
print("-"*60)
print("-- Escolha uma das funções --")
print("1) Operadores 2) Ranking 3) Dados")

escolha = input(">> Digite aqui: ")

if escolha == "1":
    funcao1()
elif escolha == "2":
    funcao2()
elif escolha == "3":
    funcao3()
else:
    print("ERRO: Opção Incorreta!")