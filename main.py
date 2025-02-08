import pygame
from pygame.locals import *
from sys import exit

import pygame.docs

pygame.init()
# variaveis tela
largura_tela = 990
meio_largura_tela = largura_tela // 2
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

#config. imagem de fundo durante game
fundo_game = pygame.image.load("sprites\\fundo_game.png")
fundo_game = pygame.transform.scale(fundo_game, (largura_tela, altura_tela))

#texto menu
mensagem = "Pressione z para começar"
fonte_menu = pygame.font.SysFont('Pixeled', 50, True, False)
start_formatado = fonte_menu.render(mensagem, False, (160, 42, 45))

#musicas
pygame.mixer.music.set_volume(0.4)
musica_menu = pygame.mixer.music.load("musicas\\overworld-day.mp3")
musica_menu = pygame.mixer.music.play(-1)
musica_game = pygame.mixer.music.load("musicas\\jungle.mp3")
musica_game = pygame.mixer.music.play(-1)

rodando = True
while rodando:
    while menu:
        tela.blit(fundo_menu, (0,0))
        tela.blit(icon, (meio_largura_tela - (icon.get_width() + 20) // 2, 10))
        tela.blit(start_formatado, (meio_largura_tela - start_formatado.get_width() // 2, 340))
        for event in pygame.event.get():
            if event.type == QUIT:
                rodando = False
                pygame.quit()
                exit()
            if event.type == KEYDOWN:
                if event.key == K_z:
                    menu = False
        pygame.display.flip()
    

    
    relogio.tick(60)
    tela.blit(fundo_game, (0, 0))
    for event in pygame.event.get():
        if event.type == QUIT:
            rodando = False
            pygame.quit()
            exit()

    


    pygame.display.flip()
