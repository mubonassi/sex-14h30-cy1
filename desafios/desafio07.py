#string -> texto (abcdef...)
#int -> numero inteiro (1,2,3...)
#float -> numero real (1.9,3.8...)

numero = int(input("Digite um número: "))

antecessor = numero - 1
sucessor = numero + 1
dobro = numero * 2
metade = numero / 2

print(f"Antecessor: {antecessor}")
print(f"Sucessor: {sucessor}")
print(f"Dobro: {dobro}")
print(f"Metade: {metade}")