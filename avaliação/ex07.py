hrsTrabalhadas = int(input("Digite as horas trabalhadas: "))
tarefasFeitas = int(input("Digite as tarefas feitas: "))

if hrsTrabalhadas >= 5 or tarefasFeitas >= 4:
    print("Você preencheu a cota necessária!")
else:
    print("Você NÃO preencheu a cota necessária!")