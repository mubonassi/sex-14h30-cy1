base = float(input("Digite a base: "))
altura = float(input("Digite a altura: "))

area = base * altura
perimetro = (base*2) + (altura*2)
diagonal = (base**2 + altura**2) ** 0.5
diferenca = base - altura

print(f"Area: {area}")
print(f"Perimetro: {perimetro}")
print(f"Diagonal: {diagonal}")
print(f"Diferença: {diferenca}")