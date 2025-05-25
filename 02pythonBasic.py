#Variaveis em Python
nome = 'Vitor'
idade = 26
peso = 67.5

#Escrevendo na tela
print('Seu nome é ' + nome + ', sua idade é', idade, 'e seu peso é', peso)

#Recebendo valores
nomerescebe = input('Qual é o seu nome? ')
idaderescebe  = input('Qual a sua idade? ')
pesorescebe = input('Qual seu peso? ')
#'\n' Quebra linha
print('Seu Nome: ', nomerescebe, '\nSua Idade: ', idaderescebe, '\nSeu Peso: ', pesorescebe)

#Opcao format
print('Olá, {}!'.format(nomerescebe))