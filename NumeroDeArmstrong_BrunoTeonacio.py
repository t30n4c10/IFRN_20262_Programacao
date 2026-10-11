# Na definição da Wikipedia, número de Armstrong é aquele número cuja soma de cada digito dele elevado a potência n
# (onde n é a quantidade de dígitos) é igual ao número informado
# (veja a definição detalhada em https://en.wikipedia.org/wiki/Narcissistic_number).

# Faça um programa que solicite ao usuário um número inteiro positivo e informe se ele é (ou não) um número de Armstrong,
# de acordo com a definição. 

# Regras:

# - Não use funções (suas ou de terceiros) para resolver a questão;
# - Faça comentários;

# Para facilitar a verificação dos dígitos, o número informado ficará como string.
# OBS: Assuma que o usuário sempre informará um número inteiro positivo.
numero = input("Digite um número inteiro positivo: ")
n_digitos = len(numero)
soma = 0

# Percorre cada dígito do número informado
for i,valor in enumerate(numero):
    # Converte o dígito de string para inteiro
    digito = int(valor)

    # Eleva o dígito à potência n_digitos e acumula na variável soma
    soma += digito ** n_digitos

# Verifica se a soma é igual ao número informado
if soma == int(numero):
    print("O número informado é um número de Armstrong.")
else:
    print("O número informado não é um número de Armstrong.")