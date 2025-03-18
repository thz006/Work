temperatura = float(input("Digite a temperatura em graus Celsius: "))
if temperatura > 30:
    print("Muito quente")
elif temperatura > 25:
    print("Quente")
elif temperatura > 15:
    print("Aconchegante")
else:
    print("Frio")