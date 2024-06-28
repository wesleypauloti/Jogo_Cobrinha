import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

pygame.mixer.music.set_volume(0.5)
musica_de_fundo = pygame.mixer.music.load('somFundo.mp3')
som_de_colisao = pygame.mixer.Sound('somdeColisao.mp3')
som_de_colisao.set_volume(1)
pygame.mixer.music.play(-1)


largura = 640
altura = 480
x_cobra = largura / 2 - (20)
y_cobra = altura / 2 - (25)
x_controle = 0
y_controle = 0
velocidade = 2
comprimento_inicial = 5
colisao = False
primeira_iteracao = True

x_maca = randint(40, 600)
y_maca = randint(50, 430)

pontos = 0
fonte = pygame.font.SysFont('arial', 40, True, True)

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Jogo")
relogio = pygame.time.Clock()

lista_cobra = []

def aumenta_cobra(lista_cobra):
    for XeY in lista_cobra:
        pygame.draw.rect(tela, (0, 255, 0), (XeY[0], XeY[1], 20, 20))
        
def reiniciar_jogo():
    global pontos, comprimento_inicial, x_cobra, y_cobra, lista_cobra, lista_cabeca, x_maca, y_maca, morreu, colisao
    pontos = 0
    comprimento_inicial = 5
    x_cobra = largura / 2 - (20)
    y_cobra = altura / 2 - (25)
    lista_cobra = []
    lista_cabeca = []
    x_maca = randint(40, 600)
    y_maca = randint(50, 430)
    morreu = False
    colisao = False

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
            if event.key == K_a or event.key == K_LEFT:
                if x_controle == velocidade:
                    pass
                else:
                    x_controle = -velocidade
                    y_controle = 0
            if event.key == K_d or event.key == K_RIGHT:
                if x_controle == -velocidade:
                    pass
                else:
                    x_controle = velocidade
                    y_controle = 0
            if event.key == K_w or event.key == K_UP:
                if y_controle == velocidade:
                    pass
                else:
                    y_controle = -velocidade
                    x_controle = 0
            if event.key == K_s or event.key == K_DOWN:
                if y_controle == -velocidade:
                    pass
                else:
                    y_controle = velocidade
                    x_controle = 0
            
    x_cobra += x_controle
    y_cobra += y_controle
    
    if not primeira_iteracao:
        for segmento in lista_cobra[0:]:
            if lista_cabeca == segmento:
                colisao = True
                break
        
    cobra = pygame.draw.rect(tela, (0, 255, 0), (x_cobra, y_cobra, 20, 20))
    maca = pygame.draw.rect(tela, (255, 0, 0), (x_maca, y_maca, 20, 20))
    
    if cobra.colliderect(maca):
        x_maca = randint(40, 600)
        y_maca = randint(50, 430)
        som_de_colisao.play()
        pontos += 1
        comprimento_inicial += 5
        velocidade += 1
        
    lista_cabeca = []
    lista_cabeca.append(x_cobra)
    lista_cabeca.append(y_cobra)    
    lista_cobra.append(lista_cabeca)
    
    if lista_cobra.count(lista_cabeca) > 6:  
        fonte2 = pygame.font.SysFont('arial', 20, True, True)
        mensagem = "Game Over! Pressione a tecla R para jogar novamente"
        texto_formatado = fonte2.render(mensagem, True, (0, 0, 0))
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
                        tela.blit(texto_formatado, (200, altura // 2))
            pygame.display.update()
        
    if x_cobra > largura:
        x_cobra = 0
    if x_cobra < 0:
        x_cobra = largura
    if y_cobra < 0:
        y_cobra = altura
    if y_cobra > altura:
        y_cobra = 0
    
    if len(lista_cobra) > comprimento_inicial:
        del lista_cobra[0]
    
    aumenta_cobra(lista_cobra)
        
    tela.blit(texto_formatado, (400, 10))
        
    pygame.display.update()



