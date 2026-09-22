# A idade média de Sara (idade 23), Mark (idade 19) e Fátima (idade 31).
nomes = ['Sara', 'Mark', 'Fatima']
idades = [23, 19 , 31]
i = 0
for i in range(3):
    print("\nNome:" + nomes[i] + " Idade:" + str(idades[i]))

print("\nMedia das idades: " + str(sum(idades)/len(idades)))

