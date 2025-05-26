#Variaveis em Python
nome = 'Vitor'
idade = 26
peso = 67.5

#Escrevendo na tela
print('Seu nome é ' + nome + ', sua idade é', idade, 'e seu peso é', peso)
print('\n--------------\n')
#Recebendo valores
nomerescebe = input('Qual é o seu nome? ')
idaderescebe  = input('Qual a sua idade? ')
pesorescebe = input('Qual seu peso? ')
#'\n' Quebra linha
print('Seu Nome: ', nomerescebe, '\nSua Idade: ', idaderescebe, '\nSeu Peso: ', pesorescebe)

#Opcao format
print('Olá, {}!\nseu peso é {}'.format(nomerescebe, pesorescebe))
print('\n--------------\n')
#Passando para int -- float -- bool-- str
n1= int(input('Vamos testar a operação de soma!\nInsira o primeiro valor: '))
n2= int(input('Segundo valor: '))
vl= n1 + n2
print('\nA soma dos valores é ', vl)
#Tipo da Variavel
tipo = input("Insira Algo: ")

print('Só espaço? ', tipo.isspace())
print('É número? ', tipo.isnumeric())
print('É Alfabeto? ', tipo.isalpha())
print('É Alphanumerico? ', tipo.isalnum())
print('Está em maiúsculo? ', tipo.isupper())
print('Está em minúsculo? ', tipo.islower())
print('Está capitalizado? ', tipo.istitle())