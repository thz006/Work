from datetime import datetime
data_validade = datetime(2024, 5, 10).date()
hoje = datetime.today().date()
if data_validade < hoje:
    print("Produto vencido")
else:
    print("Produto válido")