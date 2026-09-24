#Escreva uma instrucao Python ou instrucoes que mapeiam o primeiro e ultimo valor da lista.

time = []
loop = 1

def reverso(time_rev):
    time_rev.reverse()
    print(time_rev) #mostra a funcao inversa

while loop == 1:
    nome = str(input("Coloque um nome: "))
    time.append(nome)
    loop = int(input("Voce quer inserir mais um nome? (1 - Sim | 0 - Nao) "))

reverso(time)
