# Dado uma palavra randomica, mostra a palavra na tela em formato ------
# e revela uma letra sempre que o usuario acertar a letra da palavra.
#
# EX:
# abacate
# letra a -> a_a_a__
# letra c -> a_aca__
# letra e -> a_aca_e
# letra b -> abaca_e
# letra t -> abacate

import random

palavras = ["abacate", "ata", "animais", "ananas", "limao", "manga"]
sorteada = random.choice(palavras)
tamanho = len(sorteada)
letra_count = 0 # CONTADOR
letra_escolhida = ""
string_a_mostrar = ""

print(sorteada)
print(string_a_mostrar)
print("Palavra sorteada. Dica = A palavra tem {} letras.".format(tamanho))

while letra_count < tamanho:

    # Pede uma letra ao usuário
    letra_escolhida = input("Digite uma letra que você acha que tem na palavra sorteada: ")
    
    # Verifica se a letra escolhida está na palavra
    # OBS: Não verifica se o usuário realmente digitou uma letra.
    if letra_escolhida in sorteada:
        
        for indice, caractere in enumerate(sorteada):
        
            if caractere == letra_escolhida:
                string_a_mostrar += letra_escolhida
                
        print(string_a_mostrar)
        
        letra_count += 1
    else:
        print("A letra escolhida não faz parte da palavra. Tente novamente.")