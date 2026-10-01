#Se ano eh divisivel por 4, exiba 'Pode ser um ano bissexto.'; caso contrario, exiba 'Definitivamente nao eh um ano bissexto.

ano = int(input("Qual eh o ano: "))

if (ano % 4) == 0:
    print("Pode ser um ano bissexto.")

else:
    print("Definitivamente nao eh um ano bissexto.")
