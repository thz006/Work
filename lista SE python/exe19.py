horas_trabalhadas = float(input("Digite o número de horas trabalhadas na semana: "))
valor_hora = float(input("Digite o valor da hora normal: R$ "))

if horas_trabalhadas > 40:
    horas_normais = 40
    horas_extras = horas_trabalhadas - 40
    valor_hora_extra = valor_hora * 1.1  # 10% a mais que a hora normal
    
    salario_normal = horas_normais * valor_hora
    salario_extra = horas_extras * valor_hora_extra
    salario_total = salario_normal + salario_extra
    
    print(f"Salário total: R$ {salario_total:.2f}")
    print(f"Valor de horas extras: R$ {salario_extra:.2f}")
else:
    salario_total = horas_trabalhadas * valor_hora
    print(f"Salário total: R$ {salario_total:.2f} (sem horas extras)")