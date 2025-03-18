hora_entrada = float(input("Digite o horário de entrada (formato 24h, ex: 14.5 para 14:30): "))

if hora_entrada < 9:
    print("Entrada antecipada")
elif hora_entrada <= 12:
    print("Entrada no horário")
else:
    print("Entrada tardia")