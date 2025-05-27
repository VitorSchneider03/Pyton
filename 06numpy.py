import numpy as np

numeros = np.array([2, 4, 6, 8, 10, 20, 30, 40, 0, 1, 3, 5], np.int16)

print('Penultimo valor: {}'.format(numeros[-2]))
print('Tipo de dados é {}'.format(numeros.dtype))

num = input('Altere o Penultimo valor: ')
print('Como era: {}'.format(numeros))
numeros[-2] = num
print('Como ficou: {}'.format(numeros))