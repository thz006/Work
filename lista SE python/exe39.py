import math

raio = float(input("Digite o raio do círculo: "))

if raio > 5:
    area = math.pi * (raio ** 2)
    print(f"A área do círculo é: {area:.2f}")
else:
    print("O raio é muito pequeno para calcular a área")