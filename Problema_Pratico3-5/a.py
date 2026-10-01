#Implemente um programa que solicite do usuario uma lista de palavras (ou seja, strings) e depois exiba na tela, uma por linha, todas as strings de quatro letras nessa lista.

palavras = []

loop = 1

while loop == 1:
    inserir = str(input("Insira uma palavra "))
    palavras.append(inserir)
    loop = int(input("Deseja insirir mais um? (1 - Sim | 0 - Não) "))


for x in palavras:
    if len(x) == 4:
        print(x)
