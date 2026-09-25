#Função input() -> Recebe informação do usuário pelo terminal COMO STRING
objeto = input("Digite um objeto: ")
print(f"Você escolheu {objeto}")

num1 = int(input("Digite o numero #1: "))
num2 = float(input("Digite o numero #2: "))
conta = num1*num2
print(f"{num1}*{num2}={conta}")