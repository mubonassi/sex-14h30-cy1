#Import - Permite utilizar outras bibliotecas internas do Python
#Biblioteca - Conjunto de funções e informações

#Math - Uma biblioteca com funções matemáticas mais avançadas e especificas

#math.floor() -> arredonda para baixo - 1.5 = 1
#math.ceil() -> arredonda para cima - 1.5 = 2
#math.sqrt() -> realiza a raiz quadrada
#math.pi -> puxa a varivel constante pi
#math.inf -> puxa o valor infinito da variavel

import math

num1 = 347
num2 = 22
divisao = num1/num2
arredondado = math.floor(divisao)
print(f"Divisão Pura: {divisao} | Arredondado: {arredondado}")

valor = 140
raiz = math.sqrt(valor)
pi = math.pi
inf = math.inf
print(f"Raiz Quadrada: {raiz} | Pi: {pi} | Inf: {inf}")

#random -> biblioteca de funções que geram ou escolhem valores aleatórios
#random.randint -> gera um valor inteiro aleatório dentro de um intervalo
#random.choice

import random

valor = random.randint(1,10)
print(f"Valor aleatório: {valor}")

lista = ["a","b","c","d","e","f"]
item = random.choice(lista)
print(f"Item Aleatório: {item}")