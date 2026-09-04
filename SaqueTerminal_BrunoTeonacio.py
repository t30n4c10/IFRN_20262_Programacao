#
# Lógica:
# - Uma divisão inteira (//) de um número por outro retorna o valor inteiro do resultado;
# - Ao dividirmos o saque informado por uma das cédulas (divisão inteira) retornamos a quantidade de cédulas do tipo;
# - O resto da divisão (%) dividimos pela cedula menor a anterior;
# - Se chegarmos a 1, sabemos que o valor tem uma moeda de 1 real.
#

# Não estou usando Try/Except, então assuma que o usuário realmente digitou um número inteiro ou float.
saque = int(input("Digite o valor (R$) para o saque: "))
cedulas = [100, 50, 20, 10, 5, 2, 1] # Aqui, 1 seria a moeda de 1 real.
valor_que_resta = saque # Para o for
quantidade_cedula = [0, 0, 0, 0, 0, 0, 0] # Quantidades de cada cédula calculada.

if (saque <= 0):
    print("Informe um saque válido.")
else:

    print("Quantidade de cédulas/moedas do saque de valor R$ {}:".format(saque))

    for count, cedula in enumerate(cedulas):
    
        # Divide o valor restante do saque pela cedula (EX: 200/100 = 2 cedulas de 100)
        quantidade_cedula[count] = valor_que_resta // cedula
        # Guarda o valor que resta para a próxima divisão inteira
        valor_que_resta = valor_que_resta % cedula

    for count, quant in enumerate(quantidade_cedula):
    
        if quant > 0:
            print("Quantidade de cedulas/moedas de R$ {} igual a {}.".format(cedulas[count],quant))