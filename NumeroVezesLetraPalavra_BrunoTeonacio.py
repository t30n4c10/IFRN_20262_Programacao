# Dado uma palavra e uma letra, verifica quantas vezes a letra aparece na palavra
# OBS: NÃO usa o método count() da string.

palavra = input("Digite uma palavra: ")
letra = input("Digite uma letra: ")
contador = 0

for caractere in palavra:
    if caractere == letra:
        contador += 1

print("A letra '{}' aparece {} vezes na palavra '{}'.".format(letra, contador, palavra))