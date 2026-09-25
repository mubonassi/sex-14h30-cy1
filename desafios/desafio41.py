def conv1(celsius):
    fahrenheit = (celsius * 1.8) + 32
    return fahrenheit

def conv2(dolar):
    real = dolar * 5.35
    return real

print("-- Ferramentas de Conversão --")
print("-"*60)

print("-- Escolha uma das Opções Abaixo --")
print("1) Celsius > Fahrenheit")
print("2) Dólar > Real")

escolha = input("Digite a opção escolhida: ")

if escolha == "1":
    celsius = int(input("Digite a temperatura em ºC: "))
    fahrenheit = conv1(celsius)
    print(f"Convertido: º{fahrenheit}")
elif escolha == "2":
    dolar = float(input("Digite o valor em dolar: $"))
    real = conv2(dolar)
    print(f"Convertido: R${real}")
else:
    print("Escolha uma opção correta")