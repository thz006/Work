peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))
imc = peso / (altura ** 2)

if imc < 18.5:
    categoria = "Abaixo do peso"
elif imc < 25:
    categoria = "Peso normal"
elif imc < 30:
    categoria = "Sobrepeso"
elif imc < 35:
    categoria = "Obesidade grau 1"
elif imc < 40:
    categoria = "Obesidade grau 2"
else:
    categoria = "Obesidade grau 3"

print(f"IMC: {imc:.2f} - Categoria: {categoria}")