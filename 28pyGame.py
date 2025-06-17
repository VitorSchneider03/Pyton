import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

musica_de_fundo = pygame.mixer.music.load('Arquivos/8BitWalk.mp3')
pygame.mixer.music.play(-1)
colisao_sound = pygame.mixer.Sound('Arquivos/point.wav')

largura = 640
altura = 480
x = largura/2
y = altura/2

x_boot = randint(0, 600)
y_boot = randint(0, 430)

fonte = pygame.font.SysFont('arial', 40, True, True)
pontos = 0

relogio = pygame.time.Clock()

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Game')
while True:
    relogio.tick(300)
    mensagem = f'Pontos: {pontos}'
    texto_formatado = fonte.render(mensagem, True, (255, 255, 255))
    for event in pygame.event.get():
        tela.fill((0, 0, 0))
        if event.type == QUIT:
            pygame.quit()
            exit()
        '''
        if event.type == KEYDOWN:
            if event.key == K_a:
                x -= 20
            if event.key == K_w:
                y -= 20
            if event.key == K_d:
                x += 20
            if event.key == K_s:
                y += 20
        '''
        if pygame.key.get_pressed()[K_a]:
            if x >= 10:
                x -= 10
        if pygame.key.get_pressed()[K_w]:
            if y >= 10:
                y -= 10
        if pygame.key.get_pressed()[K_d]:
            if x <= 590:
                x += 10
        if pygame.key.get_pressed()[K_s]:
            if y <= 420:
                y += 10

        ret_player = pygame.draw.rect(tela, (100, 150, 100), (x, y, 40, 50))
        ret_boot = pygame.draw.rect(tela, (255, 0, 0), (x_boot, y_boot, 40, 50))
        if ret_player.colliderect(ret_boot):
            colisao_sound.play()
            x_boot = randint(0, 600)
            y_boot = randint(0, 430)
            pontos += 1
        tela.blit(texto_formatado, (50, 20))
        pygame.display.update()





#pygame.draw.circle(tela, (0, 0, 255), (600, 40), 40)
#pygame.draw.line(tela, (255, 255, 0), (0, 10), (300, 20), 5)