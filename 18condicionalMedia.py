s1 = float(input('Nota do primeiro semestre: '))
s2 = float(input('Nota do segundo semestre: '))
media = (s1 + s2) / 2
print('A média é de {:.1f}'.format(media))

if media >= 7:
    print('Aprovado!')
else:
    print('Reprovado!')