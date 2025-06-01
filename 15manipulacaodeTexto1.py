frase = 'A frase da atividade é Bonita!'
#Transformacao
print('Frase original:\n', frase)
#Substituir
print('\nFrase replace:\n', frase.replace('frase', 'texto'))

#CaixaAlta
print('\nFrase upper:\n', frase.upper())

#Minusculo
print('\nFrase lower\n', frase.lower())

#Apenas a primeira letra maiuscula
print('\nFrase capitalize\n', frase.capitalize())

#Titulos
print('\nFrase title:\n', frase.title())

#Removendo espaços inuteis inicio e fim
frase1 = '   Texto da atividade   '
print('\nFrase1 strip:\n', frase1.strip())

#Removendo espaços apenas Right
print('\nFrase1 rstrip:\n', frase1.rstrip())

#Removendo espaços apenas Left
print('\nFrase1 lstrip:\n', frase1.lstrip())