lista = [51,14,21,53,85,21,51]
numero = int(input("Digite um número que existe na lista: "))
tem_o_numero = 0

for i,val in enumerate(lista):
    if val == numero:
        print("A primeira posição do numero {} na lista é {}.".format(val,i))
        tem_o_numero = 1
        break

if tem_o_numero == 0:
    print("O numero {} nao pertence a lista.".format(numero))