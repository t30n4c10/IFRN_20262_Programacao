# Não estou usando Try/Except, então assuma que o usuário realmente digitou numeros float
peso = float(input("Digite o seu peso: "))
altura = float(input("Digite a sua altura: "))

IMC = round((peso/(altura**2)), 3)

if IMC < 18.5:
    print("Você está com baixo peso.")
elif IMC <= 24.9:
    print("Você está com peso normal.")
elif IMC <= 25.9:
    print("Você está com sobrepeso.")
elif IMC <= 34.9:
    print("Você está com sobrepeso grau I")
elif IMC <= 39.9:
    print("Você está com sobrepeso grau II")
else:
    print("Você está com sobrepeso grau III")