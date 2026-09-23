notas = [9, 7, 7, 10, 3, 9, 6, 6, 2]

#Uma expressao que avalia para o numero de 7 notas.
print(notas.count(7))

#Uma instrucao que muda a ultima nota para 4.
notas.insert(9, 4)
print(notas)

#Uma expressao que avalia para a nota mais alta.
notas.sort()
print(notas[-1])

#Uma instrucao que classifica as notas da lista.
print(notas)

#Uma expressao que avalia a media das notas.
print(sum(notas) / 9)
