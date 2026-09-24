'''
Escreva a fucao even() que torna um inteiro positvo n como entrada e exibe na tela todos os numeros entre 2 (inclusive)
e n, que sejam divisiveis por 2 ou por 3.
'''

def even(n_even):
    i = 2
    for i in range(n_even):
        if i % 2 == 0 or i % 3 == 0:
            print(i, end=', ')


n = eval(input("Coloque um numero: "))
even(n)
