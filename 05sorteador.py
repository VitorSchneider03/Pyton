import random

n1 = int(input('Qual o range,\nComeço: '))
n2 = int(input('Fim: '))
if n2 >= n1:
    rand = random.randint(n1, n2)
    print('Range de {} até {},\nValor sorteado é: {}'.format(n1, n2, rand))
else:
    print('Valor do RANGE invalido')