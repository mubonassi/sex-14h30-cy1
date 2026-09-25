print("| FAZENDO A TABUADA |")
print("-"*40)

tabuada = int(input("Digite o número que deseja fazer a tabuada: "))

for i in range(1,11):
    conta = tabuada * i
    print(f"{tabuada} x {i} = {conta}")