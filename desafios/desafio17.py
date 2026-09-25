print("| POSITIVO, NEGATIVO OU NEUTRO? |")
print("-"*30)

valor = int(input("Digite um valor para verificar: "))

if valor > 0:
    print(f"O valor {valor} é positivo")
elif valor < 0:
    print(f"O valor {valor} é negativo")
else:
    print(f"O valor é neutro (zero)!")