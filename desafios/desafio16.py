print("| ENTREVISTA DE EMPREGO |")
print("-"*30)

print("Responda todas as perguntas com 'sim' ou 'não'!")
print("Você veio para a entrevista de emprego?")
resposta = input("Digite aqui sua resposta: ")

if resposta == "sim":
    print("Beleza! Você trouxe o currículo?")
    resposta = input("Digite aqui sua resposta: ")
    if resposta == "sim":
        print("Afirmativo! Você tem experiência na área?")
        resposta = input("Digite aqui sua resposta: ")
        if resposta == "sim":
            print("Tudo confirmado! Podemos iniciar a entrevista!")
        else:
            print("Você precisa ter experiência na área!")
    else:
        print("Você precisa ter trazido o currículo!")
else:
    print("Pera ai, tá fazendo o que aqui, então?")