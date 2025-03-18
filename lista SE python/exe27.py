celsius = float(input("Digite a temperatura em graus Celsius: "))
fahrenheit = (celsius * 9/5) + 32

print(f"Temperatura em Fahrenheit: {fahrenheit:.2f}°F")

if celsius > 30:
    print("Calor")
else:
    print("Frio")
