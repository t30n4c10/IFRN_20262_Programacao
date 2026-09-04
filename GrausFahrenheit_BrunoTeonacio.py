# Não estou usando Try/Except, então assuma que o usuário realmente digitou um número inteiro ou float
grausCelcius = int(input("Digite uma temperatura em Graus Celcius: "))
grausFahrenheit = ((9*grausCelcius) + 160)/5
grausCelcius = input("O valor informado em Celcius, {} graus, equivale a {} graus em Fahrenheit.".format(grausCelcius,grausFahrenheit))