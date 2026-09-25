produto1 = input("Digite o #1 produto: ")
valor1 = float(input("Digite o valor do #1 produto: "))
produto2 = input("Digite o #2 produto: ")
valor2 = float(input("Digite o valor do #2 produto: "))
produto3 = input("Digite o #3 produto: ")
valor3 = float(input("Digite o valor do #3 produto: "))

valor_total = valor1 + valor2 + valor3

p_12x = valor_total / 12
p_6x = valor_total / 6
p_4x = valor_total / 4

print(f"{produto1} | R${valor1}")
print(f"{produto2} | R${valor2}")
print(f"{produto3} | R${valor3}")
print(f"Valor total: R${valor_total}")

print("--Parcelas--")
print(f"12x: R${p_12x}")
print(f"6x: R${p_6x}")
print(f"4x: R${p_4x}")