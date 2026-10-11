# Faça um programa que receba uma quantidade indeterminada de valores numéricos inteiros,
# considere que para encerrar a entrada de dados deve ser digitado o valor 0 (ZERO) e que
# ao finalizar a entrada dos valores exiba na tela o maior, o menor e a média dos valores digitados.

# - O programa deverá desconsiderar o valor 0 (ZERO) informado;
# - Não use as funções max(), min() e sum() para resolver a questão.

valores = []
maximo = 1000000000000
minimo = -1000000000000
media = 0

while 1 == 1:
    valor = int(input("Digite um valor inteiro (0 para encerrar): "))
    if valor == 0:
        break

    # Adiciona o valor informado na lista de valores
    valores.append(valor)

for i,valor in enumerate(valores):

    # No início, o maior e o menor valor são iguais ao primeiro valor informado.
    if i == 0:
        maximo = valor
        minimo = valor
    else:
        # Compara o valor com o máximo e o mínimo, além de iniciar o cálculo da média.
        if valor > maximo:
            maximo = valor
        if valor < minimo:
            minimo = valor
    media += valor

media = media / len(valores)

# Informa os resultados.
print("Maior valor informado: {}".format(maximo))
print("Menor valor informado: {}".format(minimo))
print("Média dos valores informados: {}".format(media))