lista_antiga = [5,10,12,21]
lista_nova = []

for i,val in enumerate(lista_antiga):
    if i == len(lista_antiga) - 1:
        break
    lista_nova.append(lista_antiga[i] + lista_antiga[i+1])

print(lista_nova)