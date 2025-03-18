num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if num1 > 0 and num2 > 0:
    soma = num1 + num2
    print(f"A soma dos números positivos é: {soma}")
else:
    print("A soma não pode ser realizada pois um ou ambos os números não são positivos")