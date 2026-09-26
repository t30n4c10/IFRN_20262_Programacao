# https://projecteuler.net/problem=3

number = 600851475143
divisores_primos = []

for i in range(2, number + 1):

    # Verifica se o valor em questão é primo
    is_prime = True
    for j in range(2, int(i**0.5) + 1): # Calcula até a raiz quadrada de i para otimizar a verificação
        if i % j == 0:
            is_prime = False
            break

    # Se o valor for primo e for um divisor do número em questão, adiciona à lista
    if is_prime and number % i == 0:
        divisores_primos.append(i)

print("O maior divisor primo de {} é: {}".format(number, max(divisores_primos)))