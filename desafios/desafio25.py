print("| FESTA DO TRABALHO |")
print("-"*60)

funcionarios = ["Murilo","Caio","Benjamin","Mauriceia","Patricia","Luciana","Andrew","Pietro"]
banidos = ["Andrew","Pietro"]

nome = input("Digite aqui o seu nome: ")

if nome in funcionarios:
    print(f"Seja bem vindo, {nome}!")
    if nome not in banidos:
        print("E curta a festa!")
    else:
        print("Mas, pena, você está banido. Vá embora, lembra do que fez no dia 15 de julho de 2024?")
else:
    print("Quem é você?")