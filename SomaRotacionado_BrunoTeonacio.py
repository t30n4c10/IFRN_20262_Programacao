# Para todos os números n, tais que 100 <= n < 10000, some os valores de n rotacionado. 
# O valor rotacionado de um número é tal que o seu dígito menos significativo passa a ser o mais significativo.

# Exemplos:
# - o rotacionado de 7534 é 4753
# - o rotacionado de 12345 é 51234

# Regras:
# - Não use funções (suas ou de terceiros) para resolver a questão;
# - Faça comentários;

limite_inferior = 100
limite_superior = 10000
soma_rotacionado = 0

# Percorre todos os números n no intervalo [100, 10000)
for n in range(limite_inferior, limite_superior):
    # Converte o número n para string para facilitar a manipulação dos dígitos
    numero_str = str(n)

    # Rotaciona o número: o último dígito passa a ser o primeiro
    rotacionado_str = numero_str[-1] + numero_str[:-1]

    # Converte o número rotacionado de volta para inteiro
    rotacionado = int(rotacionado_str)

    # Acumula o valor rotacionado na soma total
    soma_rotacionado += rotacionado

# Resposta: 45899550
print(soma_rotacionado)