import math #importa tudo
#from math import sqrt    importa apenas sqrt

num = int(input('Digite um número: '))
raiz = math.sqrt(num)
# se o import for preciso,  não precisa do math
#raiz = sqrt(num)
print('A raiz de {} é {:.2f}.'.format(num, raiz))