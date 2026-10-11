# Faça um programa que calcule o retorno de um investimento financeiro fazendo as contas mês a mês,
# sem usar a fórmula de juros compostos:
#
# Segue as orientações:
#
# - O programa deverá solicitar ao usuário o valor que será investido por mês e qual será o rendimento mensal;
# - O programa deve informar o saldo do investimento após um ano (soma das aplicações mês a mês considerando os juros compostos),
# e perguntar ao usuário se ele deseja que seja calculado o ano seguinte, sucessivamente;

acumulado_anual = 0
taxa_juros_mensal = 0
num_anos = 1
calculo = 'S'

while calculo == 'S':

    # Solicita as informações iniciais ao usuário
    if num_anos == 1:
        acumulado_anual = float(input("Digite o valor que será investido por mês (em R$): "))
        taxa_juros_mensal = float(input("Digite a taxa de juros mensal (em %): "))/100

    # Calcula o saldo do investimento mês a mês
    for mes in range(1, 13):
        acumulado_anual += acumulado_anual * taxa_juros_mensal

    # Mostra os valores até o momento e pergunta se deseja calcular o próximo ano
    print("O valor acumulado após o {}º ano é: R$ {}".format(num_anos, acumulado_anual))
    calculo = input("Deseja calcular mais um ano? (S/N): ").upper()

    if calculo == 'S':
        num_anos += 1