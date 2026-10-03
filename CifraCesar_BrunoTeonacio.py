# Dado uma palavra, devolve a mesma criptograafada com a cifra de César, utilizando um deslocamento definido no código.
# Assuma que a palavra não possui acentos, espaços ou caracteres especiais, e que é uma palavra válida.

palavra = input("Digite uma palavra: ")
codinome = ""
deslocamento = 1  # Definindo o deslocamento da cifra de César

for c in palavra:
    cc = chr(ord(c) + deslocamento)  # Desloca o caractere pelo valor definido
    codinome += cc  # Adiciona o caractere deslocado à nova palavra

print("A palavra criptografada é:", codinome)  # Exibe a palavra criptografada