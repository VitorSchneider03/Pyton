valor = int(input("Insira um valor inteiro para ver sua tabuada: "))
for i in range(11):
    calc = valor * i
    print('{} x {} = {}'.format(i, valor, calc))
    print('-' * 9)