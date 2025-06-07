valor = int(input('Qual sua nota na materia? '))
if valor >= 9 and valor <= 10:
    print('Bela nota, siga assim!')
elif valor >= 7 and valor < 9:
    print('Foi por pouco, mas passou!')
elif valor >=  0 and valor < 7:
    print('Ta precisando estudar mais')
else:
    print('Esse valor não me parece certo!')