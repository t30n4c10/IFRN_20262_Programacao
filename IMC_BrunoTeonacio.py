peso = float(input("Digite o seu peso: "))
altura = float(input("Digite a sua altura: "))

IMC = peso/(altura**2)

if IMC < 18.5:
    print("Você está com baixo peso.")
elif 18.5 <= IMC <= 24.9:
    print("Você está com peso normal.")
elif 25 <= IMC <= 25.9:
    print("Você está com sobrepeso.")
elif 30 <= IMC <= 34.9:
    print("Você está com sobrepeso grau I")
elif 35 <= IMC <= 39.9:
    print("Você está com sobrepeso grau II")
elif IMC > 40.0:
    print("Você está com sobrepeso grau III")