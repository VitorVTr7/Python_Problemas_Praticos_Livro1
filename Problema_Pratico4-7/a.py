'''
Escreva a funcao stringCount() que aceita duas entradas de string - um nome
de arquivo e uma string de alvo - e retorna o numero de ocorrencias da
string alvo no arquivo.
'''

def stringCount(filename, chave):
    arquivoentrada = open(filename, 'r')
    frase = arquivoentrada.read()
    arquivoentrada.close()
    return frase.count(chave)

print(stringCount('example.txt', 'ola'))
