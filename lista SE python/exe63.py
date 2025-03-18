numero = int(input("Digite um número para verificar se é primo: "))
e_primo = True

if numero <= 1:
    e_primo = False
else:
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            e_primo = False
            break

if e_primo:
    print(f"{numero} é primo")
else:
    print(f"{numero} não é primo")