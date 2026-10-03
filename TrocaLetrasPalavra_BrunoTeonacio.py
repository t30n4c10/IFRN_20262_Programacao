# Dado uma palavra, uma letra da palavra e outra letra que não pertence a palavra,
# troca todas as letras da palavra que são iguais a letra da palavra pela letra que não pertence a palavra.
# OBS: Assuma que a primeira letra está na palavra e a segunda letra não está na palavra.

palavra = input("Digite uma palavra: ")
letra_palavra = input("Digite uma letra da palavra: ")
letra_substituta = input("Digite uma letra que não pertence a palavra: ")

for i in range(len(palavra)):
    if palavra[i] == letra_palavra:

        # OBS: Em python, strings são imutáveis, então precisamos criar uma nova string com a letra substituída.
        palavra = palavra[:i] + letra_substituta + palavra[i+1:]

print("A palavra resultante após a substituição é: {}".format(palavra))