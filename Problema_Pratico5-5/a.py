'''
Escreva uma funcao acronimo() que aceite uma frase (ou seja, uma string) como entrada e
depois retorne o acronimo para essa frase.
'''

def acronimo(frase_acro):
    frase_lista = []
    frase_lista = frase_acro.upper() #Separadores
    frase_lista = frase_lista.split(" ")
    
    acronimo = ""
    for i in frase_lista:
        acronimo += (i[0])

    return acronimo





frase = str(input("Coloque o nome do componente: "))

print(acronimo(frase))
