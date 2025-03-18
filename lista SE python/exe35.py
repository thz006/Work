renda = float(input("Digite a sua renda mensal: R$ "))

if renda <= 1500:
    print("Classe baixa")
elif renda <= 5000:
    print("Classe média")
else:
    print("Classe alta")