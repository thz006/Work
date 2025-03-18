idade = int(input("Digite a idade da pessoa: "))
if idade < 12:
    print("Ingresso infantil")
elif idade <= 18:
    print("Ingresso juvenil")
else:
    print("Ingresso adulto")