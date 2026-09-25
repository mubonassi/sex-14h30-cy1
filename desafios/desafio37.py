import random
print("| CHEGANDO NO NÚMERO |")

numero = random.randint(10,100)
total = 0

while total < numero:
    escolha = int(input("Digite um número para adicionar: "))
    total += escolha

if total == numero:
    print(f"Você adicionou o número exato! Era {numero}!")
elif total > numero:
    print(f"Você passou do número! Era {numero} e você fez {total}!")
    ultrapassou = total - numero
    print(f"Você passou exatamente: {ultrapassou}")