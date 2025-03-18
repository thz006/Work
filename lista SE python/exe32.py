preco = float(input("Digite o preço da mercadoria: R$ "))

if preco > 500:
    desconto = preco * 0.2  # 20% de desconto
    preco_final = preco - desconto
    print(f"Preço com 20% de desconto: R$ {preco_final:.2f}")
else:
    desconto = preco * 0.1  # 10% de desconto
    preco_final = preco - desconto
    print(f"Preço com 10% de desconto: R$ {preco_final:.2f}")