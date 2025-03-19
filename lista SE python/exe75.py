temperatura = 10
if temperatura < 0:
    print("Frio extremo")
elif 0 <= temperatura <= 15:
    print("Frio")
elif 15 < temperatura <= 25:
    print("Aconchegante")
else:
    print("Calor")