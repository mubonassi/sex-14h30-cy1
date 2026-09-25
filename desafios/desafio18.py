print("| CONVITE DE FESTA 18+ |")

nome = input("Digite o seu nome: ")
idade = int(input("Digite a sua idade: "))
convite = input("Você tem um convite? Digite aqui: ")

if idade > 17 and convite == "sim":
    print(f"Seja bem vindo, {nome}")
else:
    print(f"Você está bloqueado e entrar, {nome}")