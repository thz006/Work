valor = float(input("Digite o valor a ser pago: R$ "))
dias = int(input("Digite quantos dias após o vencimento: "))

if dias > 30:
    valor_com_juros = valor * 1.05  # 5% de juros
    print(f"Valor com juros: R$ {valor_com_juros:.2f}")
else:
    print(f"Valor sem juros: R$ {valor:.2f}")