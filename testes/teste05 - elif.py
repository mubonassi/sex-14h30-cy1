#Estruturas de Condição -> Compostas e Encadeadas

numero = int(input("Digite um número: "))

#Estruturas de Condição Compostas
#Permite mais de uma condição na pergunta

#or -> uma das condições precisam ser verdadeiras
if numero == 5 or numero == 9:
    print("Você digitou um dos números secretos!")
else:
    print("Você NÃO digitou um dos números secretos!")

#and -> TODAS as condições precisam ser verdadeiras
if numero >= 0 and numero <= 10:
    print("Você digitou um número entre 0 a 10")
else:
    print("Você NÃO digitou um número entre 0 a 10")

#Estruturas de Condição Encadeadas
#Permite mais de uma estrutura/pergunta

#elif - pergunta sequêncial caso a anterior tenha retornado negativo
if numero > 10:
    print("Digitou um número maior que 10!")
elif numero == 10: #else if
    print("Digitou o número 10")
else:
    print("Digitou um número menor que 10!")