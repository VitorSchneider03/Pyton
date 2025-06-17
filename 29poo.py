class Pessoas:
    def __init__(self, nome, sexo, idade, peso):
        self.nome = nome
        self.sexo = sexo
        self.idade = idade
        self.peso = peso
    def comprimentar(self):
        print('Olá')

pessoa_1 = Pessoas('Pedro', 'M', 20, 60.5)

print(pessoa_1.nome)
print(pessoa_1.sexo)
pessoa_1.peso = 60

pessoa_1.comprimentar()