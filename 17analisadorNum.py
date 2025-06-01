numero = int(input('Digite um número de 0 á 9999: '))
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10

print('Analisando o número {}, sua Unidade é {}, sua Dezena é {}, sua Centena é {} e seu milhar é {}.'.format(numero, u, d, c, m))