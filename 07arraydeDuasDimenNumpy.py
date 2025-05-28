import numpy as np

m = np.array([[1, 3, 5], [2, 4, 6], [7, 9, 11], [8, 10, 12]])
print(m)
print('Número de dimensões: ', m.ndim)
print('Tamanho: ', m.shape)
print('Numero de elementos: ', m.size)
vl = input('Qual valor quer colocar: ')
l = int(input('Qual linha é: '))
c = int(input('Qual coluna é: '))
print('Como era: \n', m)
m[l,c] = vl
print('Como ficou: \n', m)

linha = int(input('Qual linha deseja visualizar? '))
coluna = int(input('Qual coluna deseja visualizar? '))
print('Linha {}, com valores: {}'.format(linha, m[linha,:]))
print('Coluna {}, com valores: {}'.format(coluna, m[:,coluna]))