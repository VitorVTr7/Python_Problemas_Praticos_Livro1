'''
Escreva uma funcao chamada potencias() que apanhe um inteiro positivo n como entrada e exiba,
na tela, todas as potencias de 2 desde 2**1 ate 2**n.
'''

def potencias(n_potencias):
    for i in range(n_potencias):
        print(2 ** (i + 1), end=" ")

loop = 1

while loop == 1:
    n = eval(input("Coloque um numero positivo: "))

    if n < 0:
        print("Numero invalido, tente novamente")
    else:
        potencias(n)
        loop = 0
