print("| CALCULO DE TEMPO DE VIAGEM |")
print("-"*30)

velocidadeMedia = float(input("> Digite a velocidade média (em km/h) percorrida: "))
distancia = float(input("> Digite a distância total da corrida (em km): "))

tempoViagem  = distancia/velocidadeMedia

print(f"Tempo total estimado: {tempoViagem}hrs")