horas_extras = float(input("Digite o número de horas extras: "))
valor_hora = float(input("Digite o valor da hora: R$ "))

if horas_extras > 40:
    valor_adicional = (horas_extras - 40) * valor_hora * 1.5
    print(f"Valor adicional a receber: R$ {valor_adicional:.2f}")
else:
    valor_adicional = horas_extras * valor_hora
    print(f"Valor adicional a receber: R$ {valor_adicional:.2f}")
