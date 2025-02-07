import pygame
from pygame.locals import *
from sys import exit

import pygame.docs

pygame.init()
# variaveis tela
largura_tela = 990
altura_tela = 555
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Legends Of The Jungle")
icon = pygame.image.load("sprites\\icon-game.png")
pygame.display.set_icon(icon)

# relogio fps
relogio = pygame.time.Clock()

# config. imagem de fundo do menu
fundo_menu = pygame.image.load("sprites\\fundo-menu.jpg").convert()
fundo_menu = pygame.transform.scale(fundo_menu, (largura_tela, altura_tela))
menu = True

#config. musica menu
pygame.mixer.music.set_volume(0.4)
musica_menu = pygame.mixer.music.load("musicas\\overworld-day.mp3")
pygame.mixer.music.play(-1)
tocando_menu = True
def musica_menu():
    if tocando_menu == False:
        pygame.mixer.music.pause()


rodando = True
while rodando:
    relogio.tick(60)
    tela.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == QUIT:
            rodando = False
            pygame.quit()
            exit()

    while menu:
        tela.blit(fundo_menu, (0,0))
        tela.blit(icon, (largura_tela // 2 - icon.get_width() // 2, 10))
        for event in pygame.event.get():
            if event.type == QUIT:
                rodando = False
                pygame.quit()
                exit()
            if event.type == KEYDOWN:
                if event.key == K_f:
                    tocando_menu = False
                    musica_menu()
                    menu = False
        pygame.display.flip()


    pygame.display.flip()
