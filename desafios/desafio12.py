print("| VERIFICADOR DE BAR |")
print("-"*30)

nome = input("Digite o seu nome: ")
idade = int(input("Digite a sua idade: "))

if (idade > 17):
    print(f"{nome}, você pode entrar no bar! Seja bem vindo!")
else:
    print(f"{nome}, você não pode entrar no bar! SAIA DAQUI!")