# Dado uma palavra, conta quantos pares consecutivos aparecem na palavra.
# OBS: Um par consecutivo é formado por duas letra seguidas de acordo com a ordem do alfabeto. Exemplo: "ab", "bc", "cd", etc.
# EX: Abacate -> 1 par consecutivo (ab)

palavra = input("Digite uma palavra: ").lower()  # Converte a palavra para minúsculas para padronizar a comparação.
contador = 0

for i in range(len(palavra) - 1):

    # Compara o valor ASCII da letra atual com a próxima letra na palavra.
    # Se a letra atual + 1 for igual à próxima letra, significa que temos um par consecutivo.

    if ord(palavra[i]) + 1 == ord(palavra[i + 1]):
        contador += 1

print("A palavra '{}' contém {} pares consecutivos.".format(palavra, contador))