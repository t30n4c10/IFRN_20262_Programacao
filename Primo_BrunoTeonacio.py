# Código não otimizado.
numero = int(input("Digite um valor: "))
num_div = 0

for cont in range(numero+1):
    
    if cont != 0 and numero % cont == 0:
        num_div = num_div + 1
        
if num_div == 2:
    print("É primo!!!")
else:
    print("Não é primo... :(")