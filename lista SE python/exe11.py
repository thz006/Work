preco = float(input("Digite o preço do produto: R$ "))

if preco > 50:
    preco_final = preco * 1.18  # acrescenta 18% de imposto
    print(f"Preço com imposto: R$ {preco_final:.2f}")
else:
    print(f"Preço sem imposto: R$ {preco:.2f}")