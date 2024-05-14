import pygame
from personagem import Personagem
from obstaculos import Obstaculo
pygame.init 

#Criando a tela
tela = pygame.display.set_mode((800, 500))
pygame.display.set_caption("Spooky-Monster")
FUNDO = pygame.image.load("imagens/fundo.png")
FUNDO = pygame.transform.scale(FUNDO, (800, 500))

#Criando personagem
monster = Personagem ("imagens/monster.png",95,110,400,387)

#criando obstaculo
aranha = Obstaculo ("imagens/aranha.png", 200,200,300,0)

rodando = True
while rodando:
    #Tratando eventos
    for evento in pygame.event.get():
        if evento.type == pygame.MOUSEBUTTONDOWN:
            print("Você clicou!!")
        if evento.type == pygame.QUIT:
            rodando = False
    tela.blit(FUNDO,(0,0))

    #Desenhando as imagens
    monster.movimentar_via_controle(pygame.K_UP,pygame.K_DOWN,pygame.K_RIGHT,pygame.K_LEFT)
    monster.desenhar(tela)
    aranha.movimenta()
    aranha.desenhar(tela)
    #Atualizando tela
    pygame.display.update()