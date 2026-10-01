'''
Escreva a funcao palavras() que aceita um argumento de entrada -
um nome de arquivo - e retorna a lista de palavras reais
(sem simbolos de pontuacao !,.:;?) no arquivo.
'''

def palavras(entrada_p):
    arquivo = open(entrada_p, 'r', encoding='utf-8')
    leitura = arquivo.read()
    arquivo.close()

    lista_resultado = []
    separador = leitura.split()

    for x in separador:
        caracteres_temp = ""          # zera a cada palavra
        for c in x:                   # percorre cada caractere
            if c.isalnum():
                caracteres_temp += c
        if caracteres_temp:           # ignora se sobrou vazio
            lista_resultado.append(caracteres_temp)

    print(lista_resultado)
    print(" ".join(lista_resultado))  # frases reescritas sem os símbolos


palavras('example.txt')

'''
Estava tendo dificuldade de realizar o objetivo final, então pedi um auxilio do
Claude em cima do "a.py" para realizar a tarefa desejada.
'''
