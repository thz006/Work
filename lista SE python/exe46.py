valor_produto = float(input("Digite o valor do produto: R$ "))

if valor_produto > 100:
    desconto = valor_produto * 0.15  # 15% de desconto
    valor_final = valor_produto - desconto
    print(f"Valor com 15% de desconto: R$ {valor_final:.2f}")
else:
    desconto = valor_produto * 0.1  # 10% de desconto
    valor_final = valor_produto - desconto
    print(f"Valor com 10% de desconto: R$ {valor_final:.2f}")