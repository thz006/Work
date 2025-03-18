salario = float(input("Digite o salário do trabalhador: R$ "))

if salario > 4000:
    imposto = salario * 0.1  # 10% de imposto
    print(f"Imposto de renda a pagar: R$ {imposto:.2f}")
else:
    print("Isento de imposto de renda")