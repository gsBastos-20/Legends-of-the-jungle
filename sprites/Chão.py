import pygame
from pygame.locals import *
import sys

pygame.init()

# Funções para o jogo
def sair_menu():
    global menu, musica_game
    menu = False
    musica_game = pygame.mixer.music.load("musicas\\jungle.mp3")
    musica_game = pygame.mixer.music.play(-1)

# Variáveis tela
largura_tela = 990
altura_tela = 555
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Legends Of The Jungle")
icon = pygame.image.load("sprites\\icon-game.png")
pygame.display.set_icon(icon)
x_pos = 0
# Relógio fps
relogio = pygame.time.Clock()

# Config. imagem de fundo do menu
fundo_menu = pygame.image.load("sprites\\fundo-menu.jpg").convert()
fundo_menu = pygame.transform.scale(fundo_menu, (largura_tela, altura_tela))
menu = True

# Config. imagem de fundo durante o jogo
fundo_game = pygame.image.load("sprites\\fundo_game.png")
fundo_game = pygame.transform.scale(fundo_game, (largura_tela, altura_tela))

# Texto menu
mensagem = "Pressione z para começar"
fonte_menu = pygame.font.SysFont('Pixeled', 50, True, False)
start_formatado = fonte_menu.render(mensagem, False, (160, 42, 45))

# Músicas
pygame.mixer.music.set_volume(0.4)
musica_menu = pygame.mixer.music.load("musicas\\overworld-day.mp3")
musica_menu = pygame.mixer.music.play(-1)

# Classe para o chão
class Chao(pygame.sprite.Sprite):
    def __init__(self, image_path, x_pos):
        super().__init__()
        # Carrega a imagem da sprite do chão
        self.image = pygame.image.load(image_path).convert_alpha()
        # Redimensiona a sprite para cobrir toda a largura da tela e a altura desejada
        self.image = pygame.transform.scale(self.image, (150, 150 ))
        # Obtém o retângulo da sprite
        self.rect = self.image.get_rect()
        # Posiciona a sprite na parte inferior da tela
        self.rect.y = altura_tela - 120
       
        self.rect.x = x_pos * 90
# Criando o chão  # Altura desejada para o chão
chao_grupo = pygame.sprite.Group()
for i in range((largura_tela * 2)  // (128 + 1)):
    chao_sprite = Chao("sprites\\chao.png", i)
    chao_grupo.add(chao_sprite)
    



rodando = True
while rodando:
    while menu:
        tela.blit(fundo_menu, (0, 0))
        tela.blit(icon, (largura_tela // 2 - (icon.get_width() + 20) // 2, 10))
        tela.blit(start_formatado, (largura_tela // 2 - start_formatado.get_width() // 2, 340))
        for event in pygame.event.get():
            if event.type == QUIT:
                rodando = False
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_z:
                    sair_menu()

        pygame.display.flip()

    relogio.tick(60)
    tela.blit(fundo_game, (0, 0))
    chao_grupo.draw(tela)  # Desenha o chão na tela

    for event in pygame.event.get():
        if event.type == QUIT:
            rodando = False
            pygame.quit()
            exit()

    pygame.display.flip()