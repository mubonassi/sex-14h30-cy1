print("| LISTA DE PRODUTOS |")
print("-"*60)
produtos = ["Coxinha","Xbox","Travesseiro","Copo de Água","Funko Pop Minion","Televisão"]

for produto in produtos:
    print(f"-- {produto}")

pedido = input("> Digite o produto desejado: ")
if pedido in produtos:
    print(f"{pedido} comprado com sucesso!")
else:
    print(f"{pedido} não está no nosso catalogo!")