# style;text;back
# style: 0=None, 1=bold, 4=underline, 7=negative
# text:  30=white,  31=red, 32=green, 33=yellow, 34=blue, 35=purple, 36=cyan, 37=gray(padrão)
# back:  40=white,  41=red, 42=green, 43=yellow, 44=blue, 45=purple, 46=cyan, 47=gray(padrão)
#\033[0;33;44m

print('\033[0;30;41mteste\033[m')
print('\033[4;33;44mteste\033[m')
print('\033[1;35;43mteste\033[m')
print('\033[30;42mteste\033[m')
print('\033[mteste\033[m')
print('\033[7;30mteste\033[m')

cores = {
    'limpa':'\033[m',
    'azul':'\033[34m',
    'verde':'\033[32m'
}
print('Está cor é {}azul{} e essa é {}verde{}.'.format(cores['azul'], cores['limpa'], cores['verde'], cores['limpa']))