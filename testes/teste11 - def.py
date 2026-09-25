#Funções -> Blocos de Código que Executam uma série de códigos para realizar alguma tarefa
#ex:
#print()
#input('escreva algo: ')
#int(valor)
## função(parametros)

#Criando Funções do Código
#def -> definição -> cria a função
#def função(parametros): ação

#Funções Simples
def exemplo1():
    n1 = 10
    n2 = 20
    res = n1+n2
    print(res)

#Chamando a função
exemplo1()

#Função com Parametros
#Parametros - São variaveis que precisam ser preenchidas por fora para o código ser executado
def exemplo2(n1,n2):
    res = n1+n2
    print(f"{n1} + {n2} = {res}")

exemplo2(10,20)
exemplo2(30,40)
exemplo2(100,200)


#Função com Return
#Permite exportar um valor/variavel da função para fora, que seja recebido por uma variavel
def exemplo3():
    n1 = 10
    n2 = 20
    res = n1+n2
    return res

resultado = exemplo3()
print(f"Resultado deu: {resultado}")

#Recebendo multiplos valores
def exemplo4():
    n1 = 56
    n2 = 29
    res = n1+n2
    return n1,n2,res

numero1,numero2,resultado = exemplo4()
print(f"{numero1} + {numero2} = {resultado}")

#Agora finalizando com parametros
def exemplo5(n1,n2):
    res = n1+n2
    return n1,n2,res

numero1,numero2,resultado = exemplo5(10,20)
print(f"{numero1} + {numero2} = {resultado}")

numero1,numero2,resultado = exemplo5(30,60)
print(f"{numero1} + {numero2} = {resultado}")