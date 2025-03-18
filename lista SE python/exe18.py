valor_compra = float(input("Digite o valor da compra: R$ "))
if valor_compra > 200:
    print(f"Total a pagar: R$ {valor_compra:.2f} (frete grátis)")
else:
    frete = 15.0
    total = valor_compra + frete
    print(f"Total a pagar: R$ {total:.2f} (incluindo frete de R$ {frete:.2f})")