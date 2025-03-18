distancia = float(input("Digite a distância da viagem (km): "))
tempo = float(input("Digite o tempo estimado da viagem (horas): "))

tempo_esperado = distancia / 80

if tempo > tempo_esperado:
    print("A viagem foi demorada")
else:
    print("A viagem foi no tempo esperado ou mais rápida")