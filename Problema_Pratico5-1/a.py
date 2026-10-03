'''
Implemente a funcao meuIMC(), que aceita como entrada a altura de uma pessoa (em metros)
e o peso (em quilos) e calcula o Indice de Massa Corporal (IMC) dessa pessoa.
A formula do IMC eh: imc = peso / altura2

Sua funcao devera exibir a string 'Abaixo do peso' se o imc < 18.5, 'Normal' se 18.5 <= imc < 25
e 'Sobrepeso' se imc >= 25.
'''

def meuIMC(peso_IMC, altura_IMC):
    soma = peso_IMC / (altura_IMC ** 2)
    if soma < 18.5:
        print("Abaixo do peso")
    elif  18.5 <= soma < 25:
        print("Normal")
    elif soma >= 25:
        print("Sobrepeso")



peso = eval(input("Insira o seu peso (em KG): "))
altura = eval(input("Insira sua altura (Em Metros): "))

meuIMC(peso, altura)
