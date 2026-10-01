'''
Comece definindo t como a hora local 1.500.000.000 segundos
a partir do início de 1 de janeiro de 1970 UTC:

Construa as proximas strings usando a função de hora em formato de string strftime():
    a) 'Thursday, July 13 2017'
    b) '9:40 PM Hora oficial do Brasil em 13/07/2017'
    c) 'Te encontro em Thu July 13 as 09:40 PM.'
'''

import time

t = time.localtime(150000000)

#a
print(time.strftime('%A, %B %d %Y', t))

#b
print(time.strftime('%I:%M %p Hora oficial do Brasil em %d/%m/%Y', t))

#c
print(time.strftime('Te encontro em %a, %B %d as %I:%M %p.', t))
