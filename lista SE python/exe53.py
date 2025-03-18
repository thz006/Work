idade = int(input("Digite a sua idade: "))
tempo_servico = int(input("Digite seu tempo de serviço em anos: "))

if idade >= 60 and tempo_servico >= 30:
    print("Você pode se aposentar")
else:
    print("Você ainda não pode se aposentar")