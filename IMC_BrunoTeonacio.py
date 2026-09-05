# Não estou usando Try/Except, então assuma que o usuário realmente digitou numeros float
peso = float(input("Digite o seu peso: "))
altura = float(input("Digite a sua altura: "))

IMC = peso/(altura**2)

if IMC < 18.500:
    print("Você está com baixo peso.")
elif 18.500 <= IMC < 24.900:
    print("Você está com peso normal.")
elif 24.900 <= IMC < 25.900:
    print("Você está com sobrepeso.")
elif 25.900 <= IMC < 34.900:
    print("Você está com sobrepeso grau I")
elif 34.900 <= IMC < 39.900:
    print("Você está com sobrepeso grau II")
elif IMC >= 39.900:
    print("Você está com sobrepeso grau III")