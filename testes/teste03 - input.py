#Recebendo Informações
#Função: input() -> Recebe uma informação do usuário pelo terminal COMO UMA STRING
#Ex: variavel = input()

nome = input("Digite o seu nome: ")
idade = input("Digite a sua idade: ")
altura = input("Digite a sua altura: ")
fruta = input("Digite a sua fruta favorita: ")
jogo = input("Digite o seu jogo favorito: ")

#Exibindo as variáveis com contexto no print
print(f"Seu nome é {nome}, você tem {idade} anos, você mede {altura}m de altura.\nSua fruta favorita é {fruta}, e seu jogo favorito é {jogo}")

#Processando/Calculando Informações na Variável
#Operando com Strings
#Ex: formando o nome completo da pessoa recebendo o nome e o sobrenome separadamente
nome = input("Digite o seu nome: ")
sobrenome = input("Digite o seu sobrenome: ")
nomeCompleto = nome + " " + sobrenome
print(f"Seu nome é {nomeCompleto}")

#Operando com Números
#Ex: somando dois números, recebendo do usuário o numero1 e o numero2, somando eles, e mostrando o resultado
#Para trabalhar com números -> Necessita conversão para int/float
#ex: int(valor) / float(valor)
numero1 = int(input("Digite um número: "))
numero2 = float(input("Digite outro número: "))
resultado = numero1+numero2 #não necessita conversão para o calculo
print(f"O resultado da soma dos valores deu {resultado}")