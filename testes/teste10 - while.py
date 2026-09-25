#Repetições Condicionadas
#Repete até a condição não for mais verdadeira
#While -> Repetir até...

numero = 0

while numero != 10:
    numero = int(input("Digite um número: "))
    if numero != 10:
        print("Mas tem que ser 10!")

#Repetição Indefinida/Infinita
#Break - Palavra chave que encerra a repetição
while True:
    escolha = input("Digite sair para sair: ")
    if escolha == "sair":
        break