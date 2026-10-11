# Dado uma lista de numeros, digitada pelo usuario, calcula o desvio padrao de todos eles.
import math

numeros = []
media = 0
desvio_padrao = 0

while 1==1:
    # Pede um numero ao usuário, para ser adicionado a lista
    numero = input("Digite um número, ou 'sair' para encerrar: ")
    if numero.lower() == 'sair':
        # Calcula a média dos números digitados
        for _,num in enumerate(numeros):
            media += num
        media = media / len(numeros)
        break
    else:
        # Adiciona o número à lista de números
        numeros.append(float(numero))
        print("Número {} adicionado à lista.".format(numero))

for i, num in enumerate(numeros):
    # Calcula o desvio padrão
    desvio_padrao += (num - media) ** 2
desvio_padrao = math.sqrt(desvio_padrao / len(numeros))
print("O desvio padrão dos números digitados é: {}".format(desvio_padrao))