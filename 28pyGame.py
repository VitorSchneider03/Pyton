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
fonte = pygame.font.SysFont('arial', 20, True, True)

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Game')
relogio = pygame.time.Clock()
lista_cobra = []
comprimento_inicial = 5
morreu = False

def aumenta_cobra(lista_cobra):
    for XeY in lista_cobra:
        #XeY = [x, y]
        #XeY[0] = x
        #XeY[1] = y

        pygame.draw.rect(tela, (100, 250, 100), (XeY[0], XeY[1], 20, 20))

def reiniciar_jogo():
    global pontos, comprimento_inicial, x_cobra, y_cobra, lista_cobra, lista_cabeca, x_maca, y_maca, morreu
    pontos = 0
    comprimento_inicial = 5
    x_cobra = int(largura / 2)
    y_cobra = int(altura / 2)
    lista_cobra = []
    lista_cabeca  = []
    x_maca = randint(0, 620)
    y_maca = randint(0, 450)
    morreu = False


while True:
    relogio.tick(45)
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

    if lista_cobra.count(lista_cabeca) > 1:
        fonte2  =pygame.font.SysFont('arial', 20, True, True)
        mensagem = 'Game over! Press R to play again!'
        texto_formatado =  fonte2.render(mensagem, True, (0, 0, 0))
        ret_texto = texto_formatado.get_rect()
        morreu = True
        while morreu:
            tela.fill((255, 255, 255))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        reiniciar_jogo()
            ret_texto.center = (largura//2, altura//2)
            tela.blit(texto_formatado, ret_texto)
            pygame.display.update()
    if x_cobra > largura - 20:
        x_cobra  = 0
    if x_cobra < 0:
        x_cobra = largura - 20
    if y_cobra < 5:
        y_cobra = altura - 20
    if y_cobra > altura - 20:
        y_cobra = 5
    if len(lista_cobra) > comprimento_inicial:
        del lista_cobra[0]
    aumenta_cobra(lista_cobra)
    tela.blit(texto_formatado, (50, 20))
    pygame.display.update()





#pygame.draw.circle(tela, (0, 0, 255), (600, 40), 40)
#pygame.draw.line(tela, (255, 255, 0), (0, 10), (300, 20), 5)