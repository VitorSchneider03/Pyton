from random import shuffle
n1  = str(input('Primeiro: '))
n2  = str(input('Segundoo: '))
n3  = str(input('Terceiro: '))
n4  = str(input('Quarto: '))
list = [n1, n2, n3, n4]
shuffle(list)
print(list)