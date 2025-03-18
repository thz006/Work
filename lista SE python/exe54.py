valor_mensalidade = float(input("Digite o valor da mensalidade: R$ "))
bolsista = input("O aluno é bolsista? (S/N): ").upper() == "S"
pagamento_antecipado = input("O pagamento será antecipado? (S/N): ").upper() == "S"

if bolsista:
    valor_final = valor_mensalidade * 0.5  # 50% de desconto
    print(f"Valor com desconto de bolsista: R$ {valor_final:.2f}")
elif pagamento_antecipado:
    valor_final = valor_mensalidade * 0.9  # 10% de desconto
    print(f"Valor com desconto de pagamento antecipado: R$ {valor_final:.2f}")
else:
    print(f"Valor sem desconto: R$ {valor_mensalidade:.2f}")