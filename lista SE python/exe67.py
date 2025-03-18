horas = float(input("Digite quantas horas o cliente ficou no estacionamento: "))
valor_diaria = float(input("Digite o valor da diária: R$ "))

if horas > 3:
    valor_final = valor_diaria * 0.9  # 10% de desconto
    print(f"Valor a pagar com desconto: R$ {valor_final:.2f}")
else:
    print(f"Valor a pagar integral: R$ {valor_diaria:.2f}")