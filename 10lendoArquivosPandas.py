import pandas as pd

arq = pd.read_csv('Arquivos/tabela_ficticia.csv', sep=';')
arq.columns = arq.columns.str.strip().str.replace('"', '')
print(arq)
print(arq.head())
print(arq.tail())
print(arq.columns)
print(arq['NOME'])