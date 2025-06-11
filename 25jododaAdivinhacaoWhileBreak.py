from random import randint
from time import sleep

pc  =  randint(0, 5)
print('-*-' * 20)
print('Estou pensando em um número inteiro entre 0 e 5. Tente acertar...')
print('-*-' * 20)
while True:

    resp = int(input('Quero ver acertar: '))
    print('Analisando-- Bip - Bop')
    sleep(1)

    if resp >= 0 and resp <= 5:
        if resp == pc:
            break
        else:
            print('Hehe, não foi dessa vez amigo(a).')
    else:
        print('Esse valor não pode!\nLeia o inunciado com  atenção!')
print(f'Parabéns, você me ganhou!\nO valor era {pc} mesmo.')