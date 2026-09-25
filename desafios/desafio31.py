print("| PARES E IMPARES |")
print("-"*60)

valor = int(input("Digite aqui o número final da sequência: "))

pares = ""
for i in range(2,valor+1,2):
    pares = pares + f"{i} "
print(f"Pares: {pares}")

impares = ""
for i in range(1,valor+1,2):
    impares += f"{i} "
print(f"Impares: {impares}")