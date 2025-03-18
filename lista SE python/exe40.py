votos_candidato1 = int(input("Digite o número de votos do candidato 1: "))
votos_candidato2 = int(input("Digite o número de votos do candidato 2: "))

if votos_candidato1 > votos_candidato2:
    print("O candidato 1 venceu a eleição")
elif votos_candidato2 > votos_candidato1:
    print("O candidato 2 venceu a eleição")
else:
    print("Houve empate na eleição")