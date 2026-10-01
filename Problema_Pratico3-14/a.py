'''
Implemente a fucao trocaPU(), que aceita uma lista como entrada e troca o primeiro e ultimo elemento da lista.
'''

def trocaPU(lista_PU):
    lista_PU[0], lista_PU[3] = lista_PU[3], lista_PU[0]
    return lista_PU

ingredientes = ['farinha', 'acucar', 'manteiga', 'macas']
print(trocaPU(ingredientes))
