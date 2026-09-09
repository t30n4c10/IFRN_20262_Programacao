# Código não otimizado.
numero = int(input("Digite um valor: "))
cont = 0
num_div = 0

while cont <= numero:
    cont = cont + 1
    
    if numero % cont == 0:
        num_div = num_div + 1
        
if num_div == 2:
    print("É primo!!!")
else:
    print("Não é primo... :(")