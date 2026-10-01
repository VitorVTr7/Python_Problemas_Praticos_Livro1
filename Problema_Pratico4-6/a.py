'''
Implemente a funcao rol(), que recebe uma lista contendo informacoes de estudantes e exibe um rol.
As informacoes do estudante, consiste em seu sobrenome, nome, nivel e nota media, serao armazenadas nessa ordem em uma lista.
Cuide para que o rol exibido tenha 10 espacos para cada valor de string e 8 para nota, incluindo 2 espacos para a parte decimal.
'''

def rol(estudantes_rol):
    print('{:10}{:10}{:10}{:10}'.format('Ultimo', 'Primeiro', 'Classe', 'Nota Media'))
    for i in estudantes_rol:
       print('{:10}{:10}{:10}{:10.2f}'.format(i[0], i[1], i[2], i[3]))

estudantes = []
estudantes.append ([ 'DeMoines', 'Jim', 'Pleno', 3.45])
estudantes.append([ 'Pierre', 'Sophi', 'Pleno', 4.0])
estudantes.append(['Columbus', 'Maria', 'Senior', 2.5])
estudantes.append(['Phoenix', 'River', 'Junior', 2.45])
estudantes.append([ 'Olympis', 'Edgar', 'Junior', 3.99])
rol(estudantes)
