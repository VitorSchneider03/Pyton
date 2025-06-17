import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

pygame.mixer.music.set_volume(0.2)
musica_de_fundo = pygame.mixer.music.load('Arquivos/8BitWalk.mp3')
pygame.mixer.music.play(-1)

colisao_sound = pygame.mixer.Sound('Arquivos/point.wav')

largura = 640
altura = 480

x_cobra = int(largura/2)
y_cobra = int(altura/2)
velocidade = 10
x_controle = velocidade
y_controle = 0

x_maca = randint(0, 620)
y_maca = randint(0, 450)

pontos = 0
fonte = pygame.font.SysFont('arial', 40, True, True)

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Game')
relogio = pygame.time.Clock()
lista_cobra = []
comprimento_inicial = 5

def aumenta_cobra(lista_cobra):
    for XeY in lista_cobra:
        #XeY = [x, y]
        #XeY[0] = x
        #XeY[1] = y

        pygame.draw.rect(tela, (100, 250, 100), (XeY[0], XeY[1], 20, 20))

while True:
    relogio.tick(30)
    tela.fill((255, 255, 255))

    mensagem = f'Pontos: {pontos}'
    texto_formatado = fonte.render(mensagem, True, (0, 0, 0))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        if event.type == KEYDOWN:
            if event.key == K_a:
                if x_controle == velocidade:
                    pass
                else:
                    x_controle = -velocidade
                    y_controle = 0
            if event.key == K_w:
                if y_controle == velocidade:
                    pass
                else:
                    y_controle = -velocidade
                    x_controle = 0
            if event.key == K_d:
                if x_controle == -velocidade:
                    pass
                else:
                    x_controle = velocidade
                    y_controle = 0
            if event.key == K_s:
                if y_controle == -velocidade:
                    pass
                else:
                    y_controle = velocidade
                    x_controle = 0

    x_cobra += x_controle
    y_cobra += y_controle
    cobra = pygame.draw.rect(tela, (100, 250, 100), (x_cobra, y_cobra, 20, 20))
    maca = pygame.draw.rect(tela, (255, 0, 0), (x_maca, y_maca, 20, 20))
    if cobra.colliderect(maca):
        colisao_sound.play()
        x_maca = randint(0, 620)
        y_maca = randint(0, 450)
        pontos += 1
        comprimento_inicial += 1
    lista_cabeca = []
    lista_cabeca.append(x_cobra)
    lista_cabeca.append(y_cobra)

    lista_cobra.append(lista_cabeca)
    if len(lista_cobra) > comprimento_inicial:
        del lista_cobra[0]
    aumenta_cobra(lista_cobra)
    tela.blit(texto_formatado, (50, 20))
    pygame.display.update()





#pygame.draw.circle(tela, (0, 0, 255), (600, 40), 40)
#pygame.draw.line(tela, (255, 255, 0), (0, 10), (300, 20), 5)