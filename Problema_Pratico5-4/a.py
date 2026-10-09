'''
Implemente a funcao fatorial(), que toma como entrada um inteiro nao negativo e retorna seu fatorial.
'''

def fatorial(n_fatorial):
    somador = n_fatorial
    if n_fatorial == 0:
        return 1
    else:
        for numero in range(1, n_fatorial):
            somador = somador * numero
        return somador

loop = True

while loop is True:
    n = eval(input("Coloque um numero: "))
    
    if n < 0:
        print("Numero negativo. Tente novamente")
    else:
        print(fatorial(n))
        loop = False


