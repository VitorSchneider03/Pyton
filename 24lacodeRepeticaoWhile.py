from random import randint
from time import sleep
value = randint(0, 5)
resp = int(input('Tente adivinhar um valor de 0 a 5: '))
while resp != value:
    print('Tente novamente')
    sleep(1)
    resp = int(input('Tente adivinhar um valor de 0 a 5: '))

print('\033[1;32mPARABENS\033[m, você acertou')