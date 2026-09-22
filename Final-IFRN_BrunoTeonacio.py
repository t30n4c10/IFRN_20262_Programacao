N1 = float(input("Digite a nota N1: "))
N2 = float(input("Digite a nota N2: "))

if (N1 <= 0) or (N2 <= 0):
    print("Digite valores válidos para as notas N1 e N2.")
else:
    
    MD = (2*N1 + 3*N2)/5
    
    if MD >= 60:
        print("Estudante aprovado por média - Média {}".format(MD))
    elif MD >= 20:

        # Assume que MFD1, MFD2 e MFD3 precisam ser iguais a 60 para passar,
        # e calcula a N3 de ambas com base nisso - N3-1, N3-2 e N3-3
        #
        # Em resumo: As formulas abaixo isolam a variavel N3 com base no MFD ser igual a 60.

        Nmenor = 0

        # Primeira NAF
        N3_1 = 120 - MD
        # Segunda NAF
        N3_2 = (300 - 3*N2)/2
        # Terceira NAF
        N3_3 = (300 - 2*N1)/3
        
        #print("As NAF são, respectivamente: {}, {} e {}".format(N3_1,N3_2,N3_3))

        # Calcula a menor das três notas - N3_1, N3_2 e N3_3
        if (N3_1 <= N3_2) and (N3_1 <= N3_3):
            Nmenor = N3_1
        elif (N3_2 <= N3_1) and (N3_2 <= N3_3):
            Nmenor = N3_2
        else:
            Nmenor = N3_3

        print("Você precisa tirar {} na prova final para passar de ano.".format(Nmenor))

    else:
        print("Estudante reprovado por média - Média {}".format(MD))
