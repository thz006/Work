tipo_produto = "eletrônicos"
preco = 1000
if tipo_produto == "eletrônicos":
    preco_com_imposto = preco * 1.18  # 18% de imposto
    print(preco_com_imposto)
else:
    preco_com_imposto = preco * 1.05  # 5% de imposto
    print(preco_com_imposto)