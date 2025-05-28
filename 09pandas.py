import pandas as pd

dados = {
    "Nome" : ["Pedro", "André", "Matheus"],
    "Idade" : [31, 33, 23],
}
df = pd.DataFrame(dados)
print(df)