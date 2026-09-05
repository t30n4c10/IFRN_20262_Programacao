N1 = float(input("Digite a nota N1: "))
N2 = float(input("Digite a nota N2: "))

if (N1 <= 0) or (N2 <= 0):
    print("Digite valores válidos para as notas N1 e N2.")
else:
    
    MD = (2*N1 + 3*N2)/5
    
    if MD >= 60:
        print("Estudante aprovado por média - Média {}".format(MD))
    elif MD >= 20:
        
        N3 = float(input("Estudante terá que fazer a prova final. Digite a nota N3: "))
        Nmaior = 0
        
        MFD1 = (MD + N3)/2 # Formato 1
        MFD2 = (2*N3 + 3*N2)/5 # Formato 2
        MFD3 = (2*N1 + 3*N2)/5 # Formato 3
        
        # Calcula a maior dentre as três notas finais - MFD1, MFD2 e MFD3
        if (MFD1 >= MFD2) and (MFD1 >= MFD3):
            Nmaior = MFD1
        elif (MFD2 >= MFD1) and (MFD2 >= MFD3):
            Nmaior = MFD2
        else:
            Nmaior = MFD3
            
        if Nmaior >= 60:
            print("Estudante aprovado por média - Média {}".format(Nmaior))
        else:
            print("Estudante reprovado por média - Média {}".format(Nmaior))
        
    else:
        print("Estudante reprovado por média - Média {}".format(MD))