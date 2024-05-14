import pygame
from personagem import Personagem
from obstaculos import Comida
pygame.init 

#Criando a tela
tela = pygame.display.set_mode((800, 500))
pygame.display.set_caption("Spooky-Monster")
FUNDO = pygame.image.load("imagens/fundo.png")
FUNDO = pygame.transform.scale(FUNDO, (800, 500))

#Criando personagem
monster = Personagem ("imagens/monster.png",95,110,400,387)

#LISTA DE COMIDA
comida = []

#criando obstaculo
aranha = Comida ("imagens/aranha.png", 100,100,20,0)
cogumelo = Comida ("imagens/olho.png", 100,180,80,0)
olho = Comida ("imagens/cogumelo.png",90,70,100,0)

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
    aranha.desenhar(tela)
    aranha.movimenta()
    cogumelo.desenhar(tela)
    cogumelo.movimenta()
    olho.desenhar(tela)
    olho.movimenta()

    #Atualizando tela
    pygame.display.update()