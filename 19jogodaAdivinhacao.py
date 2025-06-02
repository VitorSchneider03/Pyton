from random import randint
from time import sleep

pc  =  randint(0, 5)
print('-*-' * 20)
print('Estou pensando em um número inteiro entre 0 e 5. Tente acertar...')
print('-*-' * 20)
resp = int(input('Quero ver acertar: '))
print('Analisando-- Bip - Bop')
sleep(2)

if resp >= 0 and resp <= 5:
    if resp == pc:
        print('Parabéns, você me ganhou!')
    else:
        print('Hehe, não foi dessa vez amigo(a), eu pensei em {}, não em {}.'.format(pc, resp))
else:
    print('Esse valor não pode!\nLeia o inunciado com  atenção!')
