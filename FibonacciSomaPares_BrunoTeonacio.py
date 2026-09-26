# https://projecteuler.net/problem=2

term1 = 1
term2 = 2
limit = 4000000
sum = 2 # Inicia a soma com o segundo termo, que é par

while 1==1:

    # Encontra o próximo termo da sequência
    term3 = term1 + term2

    # Se o valor for maior que o limite, sai do loop
    if term3 > limit:
        break

    # Se o termo for par, adiciona ao somatório
    if term3 % 2 == 0:
        sum += term3

    term1 = term2
    term2 = term3

print("A soma dos termos pares da sequência de Fibonacci, cujos valores não ultrapassam {} é: {}".format(limit, sum))