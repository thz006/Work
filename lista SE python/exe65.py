base = float(input("Digite a base do retângulo: "))
altura = float(input("Digite a altura do retângulo: "))

if base > 10:
    area = base * altura
    print(f"A área do retângulo é: {area:.2f}")
else:
    print("O cálculo não pode ser realizado (base menor ou igual a 10)")