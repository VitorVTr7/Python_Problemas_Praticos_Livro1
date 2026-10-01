#O comprimento da hipotenusa em um triangulo retangulo cujos dois outros lados tem comprimentos a e b

import math

a = int(input("Coloque o primeiro comprimento: "))
b = int(input("Coloque o segundo comprimento: "))

hipotenusa = math.sqrt((a ** 2) + (b ** 2))

if hipotenusa == 5:
    print("Hipotenusa eh exatamamente: 5")
else:
    print("Hipotenusa eh: ", hipotenusa)

