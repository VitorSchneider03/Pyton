from pygame.examples.midi import print_device_info

text = 'Hoje é dia 01/06/2025'
text1 = 'Hoje é dia 01/06/2025 dia de domingo'

#FATIAMENTO
#Mostrando apenas um valor
print(text[5])
#Mostrando um  range
print(text[7:10])
#Desde o inicio
print(text[:4])
#Até o final
print(text[11:])
#Pulando valores
print(text[::3])
print(text[:10:3])
print(text[6::3])

#ANALISE
#Contagem de caracteres
print(text.count('0'))
#Contagem com range
print(text.count('0', 10, 21))
print(text.count('0', 15, 21))
#Conta também palavras
print(text1.count('dia'))

#Localizando textos
print(text.find('dia'))
print(text.find('Vitor')) # -1 quando não localiza

#Se existe
analise = 'dia' in text
print(analise)

analise1 = 'pneu' in text
print(analise1)
