#Estruturas de Repetição -> Permite que um bloco de código possa ser executado mais de uma vez
#Estruturas For -> Repetição contada/determinada

# i -> variavel de contagem -> i vem de "index"/"indice"
# range(x) -> determina o limite do contador

#range(3) -> [0,1,2]
for i in range(3):
    print("Teste!")
print("-- Fim de Repetição --")

#usando a variavel dentro do código
for numero in range(3):
    print(numero)
print("-- Fim de Repetição --")

for numero in range(3):
    resultado = numero + numero
    print(f"{numero} + {numero} = {resultado}")
print("-- Fim de Repetição --")

#Personalizando o range()

#Determinando o index inicial
#range(x,y) -> x: index inicial, y: index final
#[1,2,3,4,5]
for numero in range(1,6):
    print(numero)
print("-- Fim de Repetição --")

#Determinando o intervalo entre cada número
#range(x,y,z) -> x: index inicial, y: index final, z: intervalo entre cada um
#[5,10,15,20]
for numero in range(5,21,5):
    print(numero)
print("-- Fim de Repetição --")