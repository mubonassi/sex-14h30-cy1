print("| CALCULADORA COMPLETA V1 |")
print("-"*40)

numero1 = float(input("Digite o número #1: "))
numero2 = float(input("Digite o número #2: "))
print("Escolha um dos operadores: + - * / ** // %")
op = input("Digite aqui o operador: ")

if op == "+":
    resultado = numero1+numero2
elif op == "-":
    resultado = numero1-numero2
elif op == "/":
    resultado = numero1/numero2
elif op == "*":
    resultado = numero1*numero2
elif op == "**":
    resultado = numero1**numero2
elif op == "//":
    resultado = numero1//numero2
elif op == "%":
    resultado = numero1%numero2
else:
    print("Operador não existe!")
    resultado = "{{ANULADO}}"

print(f"{numero1} {op} {numero2} = {resultado}")