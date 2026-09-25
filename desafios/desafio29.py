print("| PERSONALIZANDO REPETIÇÃO |")
print("-"*60)

inicial = int(input("Digite o número inicial a ser mostrado: "))
final = int(input("Digite o número final a ser mostrado: "))

for numero in range(inicial,final+1):
    print(f"{numero}")