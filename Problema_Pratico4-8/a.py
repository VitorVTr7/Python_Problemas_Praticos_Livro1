'''
Escreva a funcao palavras() que aceita um argumento de entrada -
um nome de arquivo - e retorna a lista de palavras reais
(sem simbolos de pontuacao !,.:;?) no arquivo.
'''

def palavras(entrada_p):
    arquivo = open(entrada_p, 'r')
    leitura = arquivo.read()
    print(leitura)
    caracteres_temp = ""
    lista_resultado = []
    separador = leitura.split()
    for x in separador:
        if x.isalnum() is True:
            caracteres_temp += x
            print(caracteres_temp)
        else:
            lista_resultado.append(caracteres_temp)
            caracteres_temp = caracteres_temp.strip()


    arquivo.close
    print(lista_resultado)


palavras('example.txt')
    

