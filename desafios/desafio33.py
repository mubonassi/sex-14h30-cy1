print("| Contador de Caracteres |")
print("-"*60)

texto = input("> Digite uma palavra/frase: ")

caracteres = 0
for caractere in texto:
    if caractere != " ":
        caracteres += 1

print(f">> Total de Caracteres: {caracteres}")