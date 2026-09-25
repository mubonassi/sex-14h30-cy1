print("| MINI MERCADO |")
produto1 = input("Digite o nome do Produto 1: ")
valor1 = float(input("Digite o valor do Produto 1: "))

produto2 = input("Digite o nome do Produto 2: ")
valor2 = float(input("Digite o valor do Produto 2: "))

produto3 = input("Digite o nome do Produto 3: ")
valor3 = float(input("Digite o valor do Produto 3: "))

total = valor1 + valor2 + valor3
credito = total * 1.03
vista = total * (1 - 0.025)
#vista = total - (total * 0.025)

print(f"Produtos comprados: {produto1}; {produto2}; {produto3}")
print(f"Total: R${total}")

print("---- Formas de Pagamento ----")
print(f"Débito: R${total}")
print(f"Crédito: R${credito}")
print(f"À Vista (em dinheiro): R${vista}")