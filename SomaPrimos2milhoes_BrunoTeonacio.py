# https://projecteuler.net/problem=10
# Código não otimizado (por isso, com limite = 2000000, irá demorar muito pra executar)
# Resposta: 142913828922

soma_primos = 0
limite = 2000000
cont1 = 2 # Começa no primeiro número primo.

while cont1 < limite:

    num_div = 0
    cont2 = 1 # Para cada novo número que é verificado se é primo, esse contador precisa ser resetado.

    # O segundo while (abaixo) verifica se o número do primeiro while é primo.
    while cont2 <= cont1:

        if cont1 % cont2 == 0:
            num_div = num_div + 1

        cont2 += 1

    if num_div == 2:
        soma_primos += cont1

    cont1 += 1

print("A soma de todos os números primos abaixo de {} é: {}.".format(limite,soma_primos))