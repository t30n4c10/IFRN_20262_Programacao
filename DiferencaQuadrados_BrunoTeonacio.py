# (1^2 + 2^2 + ... + 1000^2)
soma_do_quadrado = 1

# (1 + 2 + ... + 1000)^2
quadrado_da_soma = 1

count = 1

# Soma do quadrado
while count <= 1000:
    soma_do_quadrado = soma_do_quadrado + count^2
    count += 1

count = 1

# Quadrado da soma
while count <= 1000:
    quadrado_da_soma = quadrado_da_soma + count
    count += 1
quadrado_da_soma = quadrado_da_soma**2

print(soma_do_quadrado)
print(quadrado_da_soma)

print("A diferença entre a soma dos quadrados (valor = {}) e o quadrado da soma (valor = {}) dos 1000 primeiros numeros é = {}".format(soma_do_quadrado,quadrado_da_soma,quadrado_da_soma - soma_do_quadrado))