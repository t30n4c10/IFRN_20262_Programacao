# Dado x1 e x2 (uma reta) e x3 e x4 (outra reta), determine se as retas se tocam no plano.
# Ignore Y.

reta1 = input("Digite os valores de x1 e x2 de uma das retas, separados por espaço: ").split()
reta1_x1 = int(reta1[0])
reta1_x2 = int(reta1[1])

reta2 = input("Digite os valores de x1 e x2 da outra reta, separados por espaço: ").split()
reta2_x1 = int(reta2[0])
reta2_x2 = int(reta2[1])

# Determina qual reta é 1 e qual é 2 (o usuario pode ter invertido a ordem das retas)
temp_x1 = 0
temp_x2 = 0
if reta1_x1 > reta2_x1:
    temp_x1 = reta2_x1
    temp_x2 = reta2_x2
    reta2_x1 = reta1_x1
    reta2_x2 = reta1_x2
    reta1_x1 = temp_x1
    reta1_x2 = temp_x2

# Determina se as retas informadas se encontram, ou não, no eixo X
if (reta1_x1 <= reta2_x1) and (reta1_x2 > reta2_x1):
    print("As retas informadas se encontram no eixo X.")
else:
    print("As retas informadas não se encontram no eixo X.")
