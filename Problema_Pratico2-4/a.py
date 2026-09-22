"""Escreva expressões Python usando s1, s2 e s3 e os operadores + e *
a fim de avaliar para:
a - 'ant bat cod'
b - 'ant ant ant ant ant ant ant ant ant ant'
c - 'ant bat bat cod cod cod'
d - 'ant bat ant bat ant bat ant bat ant bat ant bat ant bat'
e - 'batbatcod batbatcod batbatcod batbatcod batbatcod'
"""
s1 = 'ant'
s2 = 'bat'
s3 = 'cod'

#a
print(s1, s2, s3)

#b
print((s1 + ' ') * 10)

#c
print(s1, ((s2 + ' ') * 2) + ((s3 + ' ') * 3))

#d
print((s1 + ' ' +  s2 + ' ') * 7)

#e
print(((s2 * 2) + s3 + ' ') * 5)
