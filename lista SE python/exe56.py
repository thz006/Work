e_estudante = input("Você é estudante universitário? (S/N): ").upper() == "S"

if e_estudante:
    print("Você tem direito a 15% de desconto no transporte público")
else:
    print("Você não tem direito ao desconto no transporte público")