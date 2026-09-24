#Se a lista bilhete eh igual a lista loteria, exiba 'Voce ganhou!'; Se nao, exiba 'Melhor sorte da proxima vez...'.

loteria = [1, 2, 3, 4]

bilhete =[]
tamanho = 0
for tamanho in range(4):
    temp = eval(input("Qual eh o numero "))
    bilhete.append(temp)


if loteria == bilhete:
    print("Voce ganhou!")

else:
    print("Melhor sorte da proxima vez...")
