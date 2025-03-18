salario = float(input("Digite o salário mensal: R$ "))
if salario > 5000:
    imposto = salario * 0.15  # 15% de imposto
    print(f"Imposto a pagar: R$ {imposto:.2f}")
else:
    print("Isento de imposto")