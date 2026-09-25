qtd_litro = float(input("Quantidade de litros abastecidos: "))
valor_litro = float(input("Valor do litro: "))
dinheiro = float(input("Quanto tem em R$: "))

total = qtd_litro * valor_litro

if dinheiro >= total:
    print("Suficiente")
else:
    print("Não suficiente")