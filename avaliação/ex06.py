minutos = int(input("Minutos: "))
horas = minutos/60
dias = horas/24

print(f"Minutos: {minutos} | Horas: {horas} | Dias: {dias}")

if dias > 1:
    print("Passou mais de 1 dia")
elif dias == 1:
    print("Passou exatamente um dia")
else:
    print("Não passou 1 dia")