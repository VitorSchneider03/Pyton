n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))

soma = n1 + n2
subtracao = n1 - n2
multiplicacao = n1 * n2
divisao = n1 / n2
potencia1 = n1 ** n2
potencia2  = n2 ** n1
divisaointeira = n1 // n2
restodadivisao = n1 % n2

print('Soma é de: {}\nSubtração é de: {}\nMultiplicação é de: {}\nDivisão é de: {}\nPotência do primeiro número pelo segundo: {}\nPotência do segundo número pelo primeiro: {}\nDivisão inteira: {}\nResto da Divisão: {}'.format(soma, subtracao, multiplicacao, divisao, potencia1, potencia2, divisaointeira,  restodadivisao))
