#Array - Lista/List - Coleção de Valores

#Lista permite você guardar mais de um dado dentro da variável
lista1 = ["a","b","c","d","e","f"]
lista2 = ["abc",123,19.65,2+2,10*2,True]

#Exibindo a lista
print(lista1)
print(lista2)

#Exibindo um item especifico da lista
#Utilizando o indice (em int) do array
#print(array[x])
print(f"Item #1: {lista1[0]}")
print(f"Item #4: {lista1[3]}")

#Alterando um valor da lista
print(f"Item #3: {lista1[2]}")
lista1[2] = "Ccccccc"
print(f"Item #3: {lista1[2]}")
print(f"Lista Final: {lista1}")

#Recebendo um valor para alterar
#indice = int(input("Digite o item que deseja alterar: "))
#valor = input("Digite o novo valor do item: ")
#lista1[indice] = valor
#print(f"Lista: {lista1}")

#Verificando um valor na lista
valor = "a"
valor2 = "x"

#comparador "in"
if valor in lista1:
    print("O valor está na lista")

if valor2 not in lista1:
    print("O valor não está na lista")