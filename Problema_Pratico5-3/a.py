'''
Escreva a funcao aritmetica(), que aceita uma lista de inteiros como entrada e retorna True se eles formarem
uma sequencia aritmetica. (Uma sequencia de inteiros eh uma sequencia aritmetica se a diferenca
entre os itens consecutivos da lista for sempre a mesma.)
'''
import os

def aritmetica(lista_arit):
    if len(lista_arit) == 1:
        return True
    else:
        for i in range(0, len(lista_arit) - 1):
            if lista_arit[0] % lista_arit[i] != 0:
                return False

        return True

lista = []
loop = 1
while loop == 1:
    valor = eval(input("Coloque um numero na posicao {}: ".format((len(lista) + 1))))
    lista.append(valor)
    loop = eval(input("Deseja inserir mais algum numero? (0 - Nao | 1 - Sim): "))
    os.system('cls||clear')

print(aritmetica(lista))

