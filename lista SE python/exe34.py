dia = int(input("Digite um número entre 1 e 7: "))
dias_semana = {
    1: "Domingo", 2: "Segunda-feira", 3: "Terça-feira", 4: "Quarta-feira",
    5: "Quinta-feira", 6: "Sexta-feira", 7: "Sábado"
}

if 1 <= dia <= 7:
    print(f"O dia correspondente é: {dias_semana[dia]}")
else:
    print("Número inválido. Digite um número entre 1 e 7.")