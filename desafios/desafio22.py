print("| COMPRANDO PRODUTOS |")

produtos = ["Xbox","Playstation","Nintendo Switch","Batata Frita","Coxinha","Refrigerante","Televisão"]
valores = [2000,5500,3800,10,15,9,5000]


print(f"Lista de produtos disponíveis: {produtos}")

escolha = int(input("Digite o produto desejado (indice): "))

print(f"Você escolheu o produto {produtos[escolha]}! E seu valor é R${valores[escolha]}")

print("Deseja comprar o produto? Sim ou não?")
comprar = input("Digite aqui: ")

if comprar == "sim":
    produtos[escolha] = "(COMPRADO)"
else:
    print("Então, ok, flw")

print(f"Lista final de produtos: {produtos}")