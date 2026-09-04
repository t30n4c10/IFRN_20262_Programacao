# Não estou usando Try/Except, então assuma que o usuário realmente digitou numeros float
peso = float(input("Digite o seu peso: "))
altura = float(input("Digite a sua altura: "))

IMC = peso/(altura**2)

if IMC < 18.5:
    print("Você está com baixo peso.")
elif 18.5 <= IMC < 24.9:
    print("Você está com peso normal.")
elif 24.9 <= IMC < 25.9:
    print("Você está com sobrepeso.")
elif 25.9 <= IMC < 34.9:
    print("Você está com sobrepeso grau I")
elif 34.9 <= IMC < 39.9:
    print("Você está com sobrepeso grau II")
elif IMC >= 39.9:
    print("Você está com sobrepeso grau III")