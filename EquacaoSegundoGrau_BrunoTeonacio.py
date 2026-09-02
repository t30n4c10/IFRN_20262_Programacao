#import math # Para usar a raiz quadrada

valores = input("Digite os valores de a, b e c, de uma equação do segundo grau (separados por espaço):").split()
a = int(valores[0])
b = int(valores[1])
c = int(valores[2])
delta = 0
x1 = 0
x2 = 0

if a == 0:
    print("O valor de a não pode ser zero. Envie novamente os valores.")
else:
    delta = (b**2) - (4*a*c)

    if delta < 0:
        print("O valor de delta da equação, {}, é menor que 0, portanto as raízes são imaginárias.".format(delta))
    else:    
        #x1 = (-b + math.sqrt(delta))/(2*a)
        #x2 = (-b - math.sqrt(delta))/(2*a)
        x1 = (-b + delta**0.5)/(2*a)
        x2 = (-b - delta**0.5)/(2*a)


        print("A equação de segundo grau informada possui as raízes {} e {}.".format(x1,x2))