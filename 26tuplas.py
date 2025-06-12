cardapio = 'batata', 'arroz', 'feijão', 'bife'
bebida = 'suco','refrigerante'
todo = cardapio + bebida #uniao de tuplas
print(todo)
print(cardapio)
print(sorted(cardapio))
print(cardapio[2])
for alimento in cardapio:
    print(f'O prato contem {alimento}')



for posicao, alimento in enumerate(cardapio):
    print(f'A comida {alimento}, está na posição {posicao}')