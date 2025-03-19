fatura_paga = True
data_vencimento = datetime(2025, 3, 15).date()
if fatura_paga and data_vencimento < hoje:
    print("Multa de 5% por atraso")
else:
    print("Pagamento no prazo")