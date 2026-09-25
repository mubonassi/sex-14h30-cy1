def conv1(cel):
    fah = (cel * 1.8) + 32
    print(f"Convertido: {fah}ºF")

def conv2(dolar):
    real = dolar * 5.35
    return real

def conv3():
    km = float(input("Digite a distÂncia em km: "))
    m = km * 1000
    print(f"Convertido: {m}m")


print("-- Ferramentas de Conversão --")
print("-"*60)

while True:
    print("-- Escolha uma das Opções Abaixo --")
    print("1) Celsius > Fahrenheit")
    print("2) Dólar > Real")
    print("0) Sair")

    escolha = input("Digite a opção escolhida: ")

    if escolha == "1":
        celsius = int(input("Digite a temperatura em ºC: "))
        conv1(celsius)
    elif escolha == "2":
        dolar = float(input("Digite o valor em dolar: $"))
        real = conv2(dolar)
        print(f"Convertido: R${real}")
    elif escolha == "3":
        conv3()
    elif escolha == "0":
        break
    else:
        print("Escolha uma opção correta")