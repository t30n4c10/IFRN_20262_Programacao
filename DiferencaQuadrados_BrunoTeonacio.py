# https://projecteuler.net/problem=6
# Código não otimizado

# (1^2 + 2^2 + ... + 1000^2)
soma_do_quadrado = 0

# (1 + 2 + ... + 1000)^2
quadrado_da_soma = 0

count = 1
limite = 100

# Soma do quadrado
while count <= limite:
    soma_do_quadrado = soma_do_quadrado + count**2
    count += 1

count = 1

# Quadrado da soma
while count <= limite:
    quadrado_da_soma = quadrado_da_soma + count
    count += 1
quadrado_da_soma = quadrado_da_soma**2 # Note que essa linha está fora do while.

# Quadrado da soma é SEMPRE maior que a soma dos quadrados
print("A diferença entre a soma dos quadrados (valor = {}) e o quadrado da soma (valor = {}) dos {} primeiros numeros é = {}".format(soma_do_quadrado,quadrado_da_soma,limite,quadrado_da_soma - soma_do_quadrado))