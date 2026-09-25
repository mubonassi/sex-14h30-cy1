print("| LOGANDO NO SISTEMA |")
print("-"*60)
usuarios = ["Murilo","Admin","Chefe","Normal","Sei lá"]
tentativa = ""

while tentativa not in usuarios:
    tentativa = input(">> Digite aqui o nome do usuário: ")
    if tentativa == "sair":
        print("Saindo do sistema...")
        break

total = 0
if tentativa in usuarios:
    while True:
        print("-"*60)
        print(f"-- TOTAL: {total} --")
        print("ESCOLHA UMA DAS OPÇÕES: 1) Adicionar 2) Subtrair 3) Resetar 0) Sair")
        escolha = input("Digite aqui: ")

        if escolha in ["1","2"]:
            valor = int(input("Digite um valor: "))

        if escolha == "1":
            total += valor
        elif escolha == "2":
            total -= valor
        elif escolha == "3":
            total = 0
            print(">> AVISO: VALOR RESETADO <<")
        elif escolha == "0":
            break
        else:
            print("Escolha uma opção correta!")