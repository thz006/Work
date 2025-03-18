valor_compra = float(input("Digite o valor da compra: R$ "))
if valor_compra > 100:
    valor_final = valor_compra * 0.9  # aplica 10% de desconto
    print(f"Valor com desconto: R$ {valor_final:.2f}")
else:
    print(f"Valor sem desconto: R$ {valor_compra:.2f}")