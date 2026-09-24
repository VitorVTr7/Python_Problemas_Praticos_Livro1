'''
Escreva instrucoes python correspondentes a estas atribuicoes:
a) a variavel cont, a quantidade de ocorrencias da string 'day' na string previsao
b) a variavel clima, o indice em que substring 'sunny' comeca
c) A variavel troca, uma copia da previsao na qual cada ocorrencia da substring 'sunny' eh substituida por 'cloudy'
'''

previsao = 'It will be a sunny day today'

#a
cont = previsao.count('day')

#b
clima = previsao.find('sunny')

#c
troca = previsao
troca = troca.replace('sunny', 'cloudy')


print('a: ', cont)
print('b: ', clima)
print('c: ', troca)
