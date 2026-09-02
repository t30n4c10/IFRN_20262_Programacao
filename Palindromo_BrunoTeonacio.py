# Não estou usando Try/Except, então assuma que o usuário realmente digitou um número inteiro.
numero_original = int(input("Digite um número: "))
numero = numero_original
x = 0

while numero != 0:
    x = x*10 + numero%10
    numero = numero//10
    
if x == numero_original:
    print("O numero {} é um palíndromo.".format(numero_original))
else:
    print("O numero {} não é um palíndromo.".format(numero_original))