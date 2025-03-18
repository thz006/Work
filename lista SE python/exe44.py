valor_boleto = float(input("Digite o valor do boleto: R$ "))
data_vencimento_passou = input("O boleto já venceu? (S/N): ").upper() == "S"

if data_vencimento_passou:
    multa = valor_boleto * 0.02  # 2% de multa
    valor_final = valor_boleto + multa
    print(f"Valor com multa: R$ {valor_final:.2f}")
else:
    print(f"Valor sem multa: R$ {valor_boleto:.2f}")