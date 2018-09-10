'''Geovanna Alves
data: 21/08
'''

lista = list()
for n in range(5):
    numero = int(input('Digite um {} numero :' .format(n+1)))
    lista.append(numero)

maior = max(lista)
menor = min(lista)
pos_max = lista.index(maior)
pos_min = lista.index(menor)

print('O maior numero digitado foi {} que \ esta na posição{}.'.format(maior,pos_max))
print('O menor numero digitado foi {} que \ esta na posição{}.'.format(menor,pos_min))
    
