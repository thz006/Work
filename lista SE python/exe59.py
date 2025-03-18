gols_time_a = int(input("Digite o número de gols do time A: "))
gols_time_b = int(input("Digite o número de gols do time B: "))

if gols_time_a > gols_time_b:
    print("Time A venceu o jogo")
elif gols_time_b > gols_time_a:
    print("Time B venceu o jogo")
else:
    print("Empate")