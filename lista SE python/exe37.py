nota = float(input("Digite uma nota de 0 a 10: "))

if nota < 2:
    print("Nota Muito Baixa")
elif nota < 4:
    print("Nota Baixa")
elif nota < 6:
    print("Nota Média")
elif nota < 8:
    print("Nota Boa")
else:
    print("Nota Excelente")