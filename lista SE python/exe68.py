antecipado = input("O ingresso foi comprado antecipadamente? (S/N): ").upper() == "S"
preco_normal = float(input("Digite o preço normal do ingresso: R$ "))

if antecipado:
    preco_final = preco_normal * 0.9  # 10% de desconto
    print(f"Preço do ingresso com desconto: R$ {preco_final:.2f}")
else:
    print(f"Preço do ingresso normal: R$ {preco_normal:.2f}")