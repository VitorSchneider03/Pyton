import pandas as pd

arq = pd.read_csv('Arquivos/tabela_ficticia.csv', sep=';')
arq.columns = arq.columns.str.strip().str.replace('"', '')
print(arq)

arq['DAQUI_5_ANOS'] = arq['IDADE'] + 5


maior_de_30 = arq['IDADE'] > 30
vendedores = arq['FUNCAO'] == 'Vendedor'
maior_de_25 = arq['DAQUI_5_ANOS'] > 30
print('\n\n Vendedores maiores de 30 anos:\n', arq[maior_de_30 & vendedores])
print('\n\n Vendedores maiores de 30 em 5 anos:\n', arq[maior_de_25 & vendedores])
nomes = arq.loc[maior_de_30 & vendedores, 'NOME'].tolist()
print('\n\nVendedores maiores de 30 anos:\n', nomes)
print('\n\n', arq['FUNCAO'].value_counts())
print('Média de idade:\n', arq.groupby('FUNCAO')['IDADE'].mean())
print('Idade Máxima por setor:\n', arq.groupby('FUNCAO')['IDADE'].max())
print('\n\n\nOrdenando por idade:\n', arq.sort_values(by='IDADE', ascending=False))

#usar função merge para vincular duas tabelas