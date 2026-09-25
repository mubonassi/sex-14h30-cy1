print("| POSTO DE PYTHON-LINA! |")
print("-"*30)

abastecido = float(input("Digite o quanto foi abastecido (em L): "))
valorGasolina = float(input("Digite o preço do litro da gasolina: R$"))
total = abastecido*valorGasolina

print(f"| Valor total: R${total}")

pagamento = float(input("Digite o quanto está dando em dinheiro: R$"))

if pagamento < total:
    print("ERRO! Valor insuficiente!")
else:
    print("Pagamento realizado com sucesso!")
    if pagamento > total:
        troco = pagamento - total
        print(f"Troco: R${troco}")