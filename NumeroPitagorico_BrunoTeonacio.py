# https://projecteuler.net/problem=9
# Código não otimizado.

for a in range(1, 1001):
    for b in range(a + 1, 1001):
        c = 1000 - a - b

        # Mostra os números pitagóricos (a, b, c) cuja soma é 1000 e o produto deles.
        if (c > b) and (a**2 + b**2 == c**2):
            print("a = {}, b = {}, c = {}, a*b*c = {}".format(a,b,c,a*b*c))