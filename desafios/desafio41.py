def conv1(cel):
    fah = (cel * 1.8) + 32
    return fah

def conv2(dol):
    real = dolar * 5.35
    return real

def conv3(m):
    km = m/1000
    return km

def conv4(mb):
    gb = mb/1024
    return gb

def conv5(min):
    hr = min/60
    return hr

def conv6(hrs):
    dias = hrs/24
    return dias


print("-- Ferramentas de Conversão --")
print("-"*60)

while True:
    print("-- Escolha uma das Opções Abaixo --")
    print("1) Celsius > Fahrenheit")
    print("2) Dólar > Real")
    print("3) Metros > Quilometros")
    print("4) Megabytes > Gigabytes")
    print("5) Minutos > Horas")
    print("6) Horas > Dias")
    print("0) Sair")

    escolha = input("Digite a opção escolhida: ")

    if escolha == "1":
        celsius = int(input("Digite a temperatura em ºC: "))
        fahrenheit = conv1(celsius)
        print(f"Convertido: {fahrenheit}ºF")
    elif escolha == "2":
        dolar = float(input("Digite o valor em dolar: $"))
        real = conv2(dolar)
        print(f"Convertido: R${real}")
    elif escolha == "3":
        metros = float(input("Digite o valor em Metros: "))
        quilometros = conv3(metros)
        print(f"Convertido: {quilometros}km")
    elif escolha == "4":
        mega = float(input("Digite o valor em mega: "))
        giga = conv4(mega)
        print(f"Convertido: {giga}gb")
    elif escolha == "5":
        minutos = float(input("Digite o valor em minutos: "))
        horas = conv5(minutos)
        print(f"Convertido: {horas}hrs")
    elif escolha == "6":
        horas = float(input("Digite o valor em horas: "))
        dias = conv6(horas)
        print(f"Convertido: {dias} dias")
    elif escolha == "0":
        break
    else:
        print("Escolha uma opção correta")