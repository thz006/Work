bebida = input("Escolha uma bebida (Coca-Cola, Cerveja, Água): ").lower()

if bebida == "coca-cola":
    print("Refrigerante")
elif bebida == "cerveja":
    print("Álcool")
elif bebida == "água" or bebida == "agua":
    print("Bebida saudável")
else:
    print("Bebida não reconhecida")