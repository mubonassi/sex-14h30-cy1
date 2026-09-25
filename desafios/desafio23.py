print("| AUTENTICAÇÃO DE USUÁRIO |")
print("-"*60)

usuarios = ["Admin","Murilo","Benjamin","Caio","Python","Sei lá mais quem"]

usuario = input("Digite aqui o nome do seu usuário: ")

if usuario in usuarios:
    print(f"Usuário {usuario} autenticado com sucesso!")
else:
    print(f"Usuário {usuario} não existe no sistema!")