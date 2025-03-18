calorias = float(input("Digite o número de calorias do alimento: "))

if calorias < 100:
    print("Baixas Calorias")
elif calorias < 300:
    print("Média Caloria")
else:
    print("Alta Caloria")