soma_idades = 0

for i in range(1, 6):
    idade = int(input(f"Digite a idade da {i}ª pessoa: "))
    soma_idades += idade

media_idades = soma_idades / 5

print(f"A média das idades é: {media_idades:.2f} anos")

if media_idades > 30:
    print("A média é maior que 30 anos")
else:
    print("A média é menor ou igual a 30 anos")