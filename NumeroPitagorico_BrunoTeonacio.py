# Encontre um trio de numeros pitagoricos, 'a' 'b' e 'c', tal que a + b + c = 1000
# Range de a -> 1 a 1000
# Range de b -> 1+1 (um valor a frente) até 1000
# Código não otimizado.

for a in range(1, 1001):
    for b in range(a + 1, 1001):
        c = 1000 - a - b

        if a**2 + b**2 == c**2:
            print("a = {}, b = {}, c = {}".format(a,b,c))