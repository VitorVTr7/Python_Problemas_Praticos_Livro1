# Se golpes eh maior que 10 e defesas e 0, exiba 'Voce esta morto...'.

golpes = eval(input("Quantos golpes tomados? "))
defesa = eval(input("Quanto de defesa? "))

if golpes > 10 and defesa <= 0:
    print("Voce esta morto")
else:
    print("Continue lutando")

