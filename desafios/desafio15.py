print("| ADIVINHANDO A SENHA NUMÉRICA |")
print("-"*30)

senha = 1234

tentativa = int(input("Digite a sua tentativa de senha: "))

if tentativa == senha:
    print("Você acertou a senha secreta!!")
else:
    if tentativa > senha:
        print("Você tentou um número maior que a senha!")
    else:
        print("Você tentou um número menor que a senha!")