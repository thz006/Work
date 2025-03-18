numero = int(input("Digite um número: "))
fatorial = 1

if numero > 0:
    for i in range(1, numero + 1):
        fatorial *= i
    print(f"O fatorial de {numero} é {fatorial}")
else:
    print("Não é possível calcular o fatorial de números negativos")