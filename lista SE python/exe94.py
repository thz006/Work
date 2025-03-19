temperaturas = [25, 30, 27, 28, 29, 32, 31]
media = sum(temperaturas) / len(temperaturas)
if media > 25:
    print("Semana quente")
else:
    print("Semana fria")