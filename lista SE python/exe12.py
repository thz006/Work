peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))
imc = peso / (altura ** 2)

if imc < 18.5:
    classificacao = "Abaixo do peso"
elif imc < 25:
    classificacao = "Peso normal"
elif imc < 30:
    classificacao = "Sobrepeso"
elif imc < 35:
    classificacao = "Obesidade grau 1"
elif imc < 40:
    classificacao = "Obesidade grau 2"
else:
    classificacao = "Obesidade grau 3"

print(f"IMC: {imc:.2f} - Classificação: {classificacao}")