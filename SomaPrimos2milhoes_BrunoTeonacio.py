# https://projecteuler.net/problem=10
# Código não otimizado

soma_primos = 0
limite = 100
cont1 = 2 # Primeiro while
cont2 = 0 # Segundo while

while cont1 < limite:

    #print("cont1 = {}".format(cont1))
    num_div = 0

    while cont2 < limite:
        #print(cont2)
        if cont2 != 0 and cont1 % cont2 == 0:
            num_div = num_div + 1
        cont2 += 1

    if num_div == 2:
        soma_primos += cont1

    cont1 += 1

print(soma_primos)