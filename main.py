import pygame
from pygame.locals import *
import sys
import os
from random import randrange
pygame.init()

# diretorios
diretorio_principal = os.path.dirname(__file__)
diretorio_sprites = os.path.join(diretorio_principal, "sprites")
diretorio_musicas = os.path.join(diretorio_principal, "musicas")

#funções para o jogo
def sair_menu():
    global menu, musica_game
    menu = False
    musica_game = pygame.mixer.music.load("musicas\\jungle.mp3")
    musica_game = pygame.mixer.music.play(-1)

# variaveis tela
largura_tela = 990
meio_largura_tela = largura_tela // 2
altura_tela = 555
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Legends Of The Jungle")
icon = pygame.image.load(os.path.join(diretorio_sprites, "icon-game.png")).convert_alpha()
pygame.display.set_icon(icon)


# relogio fps
relogio = pygame.time.Clock() 
# config. imagem de fundo do menu
fundo_menu = pygame.image.load(os.path.join(diretorio_sprites, "fundo-menu.jpg")).convert()
fundo_menu = pygame.transform.scale(fundo_menu, (largura_tela, altura_tela))
menu = True

#config. imagem de fundo durante game
fundo_game = pygame.image.load(os.path.join(diretorio_sprites, "fundo_game.png")).convert()
fundo_game = pygame.transform.scale(fundo_game, (largura_tela, altura_tela))

#texto menu
mensagem = "Pressione z para começar"
fonte_menu = pygame.font.SysFont('Pixeled', 50, True, False)
start_formatado = fonte_menu.render(mensagem, False, (160, 42, 45))

#musicas
pygame.mixer.music.set_volume(0.4)
musica_menu = pygame.mixer.music.load(os.path.join(diretorio_musicas, "overworld-day.mp3"))
musica_menu = pygame.mixer.music.play(-1)


#Objetos
todas_as_sprites = pygame.sprite.Group()
for i in range(3):
    bird = Birds()
    todas_as_sprites.add(bird)

for i in range((largura_tela*2) // 128):
    chao = Chao(i)
    todas_as_sprites.add(chao)

jogador = Player(100)
todas_as_sprites.add(jogador)
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
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_z:
                    sair_menu()
        
        pygame.display.flip()
    

    relogio.tick(45)
            
    
    relogio.tick(60)
    tela.blit(fundo_game, (0, 0))
    for event in pygame.event.get():
        if event.type == QUIT:
            rodando = False
            pygame.quit()
            exit()

    if pygame.key.get_pressed()[K_a]:
        jogador.andar()
    if pygame.key.get_pressed()[K_d]:
        jogador.andar()
    todas_as_sprites.draw(tela)
    todas_as_sprites.update()


    

    pygame.display.flip()