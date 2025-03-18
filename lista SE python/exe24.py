numero_mes = int(input("Digite um número de 1 a 12: "))
meses = {
    1: "Janeiro", 2: "Fevereiro", 3: "Março", 4: "Abril",
    5: "Maio", 6: "Junho", 7: "Julho", 8: "Agosto",
    9: "Setembro", 10: "Outubro", 11: "Novembro", 12: "Dezembro"
}

if 1 <= numero_mes <= 12:
    print(f"O mês correspondente é: {meses[numero_mes]}")
else:
    print("Número inválido. Digite um número de 1 a 12.")