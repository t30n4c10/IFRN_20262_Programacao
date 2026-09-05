salario = float(input("Informe o seu salário: "))
IRPF = 0

# Primeiro cálculo
if salario <= 2428.80:
    print("Não precisa pagar imposto de renda.")
elif salario <= 2826.65:
    IRPF = salario*0.075 - 182.16
elif  salario <= 3751.05:
    IRPF = salario*0.15 - 394.16
elif salario <= 4664.68:
    IRPF = salario*0.225 - 675.49
elif salario > 4664.68:
    IRPF = salario*0.275 - 908.73
    
# Segundo cálculo
if salario <= 5000:
    
    # Na prática, deve "zerar" o IRPF
    IRPF = IRPF - 312.89
    
elif salario <= 7350:
    
    # Redução progressiva, de acordo com o salário
    IRPF = 978.62 - (0.133145*salario)

if IRPF > 0:
    print("Seu IRPF a pagar será {}.".format(IRPF))
else:
    print("Não precisa pagar imposto de renda.")