temperatura = float(input("Digite a temperatura do ambiente: "))

if temperatura >= 16 and temperatura <= 25:
    print("Temperatura está boa!")
elif temperatura > 25:
    print("Temperatura está muito quente!")
elif temperatura < 16:
    print("Temperatura está muito fria")