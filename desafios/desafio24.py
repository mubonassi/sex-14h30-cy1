print("| SORVETERIA PYTHON |")
print("-"*60)

sabores = ["Chocolate","Flocos","Morango","Napolitano","Creme"]
coberturas = ["Flocos","MMs","Fini","Chocolate quente","Leite Condensado"]

print(f"Sabores disponíveis: {sabores}")
print(f"Coberturas disponíveis: {coberturas}")

sabor = input("Digite aqui o sabor escolhido: ")

if sabor in sabores:
    cobertura = input("Digite aqui a cobertura: ")
    if cobertura in coberturas:
        print(f"O pedido sorvete de {sabor} com {cobertura} foi finalizado!")
    else:
        print(f"A cobertura {cobertura} não existe! Então, ficará só o sorvete de {sabor}")
else:
    print(f"Sabor {sabor} não existente no cardápio!")