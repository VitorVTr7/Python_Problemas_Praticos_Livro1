i = 1
valor = 403
contador = 0
while i == 1 :
    if valor > 0:
        valor -= 73
        contador += 1
    else:
        i = 0


print("Ele caberá " + str(contador - 1))

