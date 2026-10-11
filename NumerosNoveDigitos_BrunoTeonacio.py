# Quantos números de exatos 9 dígitos existem que não possuem três dígitos consecutivos que cuja soma seja maior que 8?
#
# Regras:
#
# - Não use funções (suas ou de terceiros) para resolver a questão;
# - Faça comentários.

limite_inferior = 100000000 # 100 milhões, menor número de 9 dígitos.
limite_superior = 1000000000 # 1 bilhão, menor número de 10 dígitos.
contador = 0
soma_permitida = 8

# A conta inicia no limite inferior e vai até o limite superior.
for numero in range(limite_inferior, limite_superior):

    # Converte o número em uma string para facilitar a verificação dos dígitos
    numero_str = str(numero)
    
    # Verifica se há três dígitos consecutivos cuja soma seja maior que soma_permitida
    possui_tres_consecutivos = False
    for i in range(len(numero_str) - 2):

        # Note o (len(numero_str) - 2) no range, isso é para evitar o erro de índice fora do intervalo,
        # já que estamos somando três dígitos consecutivos.
        soma_consecutivos = int(numero_str[i]) + int(numero_str[i + 1]) + int(numero_str[i + 2])
        
        if soma_consecutivos > soma_permitida:
            possui_tres_consecutivos = True
            break
    
    # Se não possui três dígitos consecutivos cuja soma seja maior que soma_permitida, incrementa o contador
    if possui_tres_consecutivos == False:
        contador += 1

# Resposta: 1709730 números.
# OBS: Código não otimizado, então vai demorar muito pra executar. Tenha paciência.
print("O número de números de 9 dígitos que não possuem três dígitos consecutivos cuja soma seja maior que {} é: {}".format(soma_permitida, contador))