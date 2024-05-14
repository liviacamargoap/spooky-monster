import pygame
pygame.init 

#Criando a tela
tela = pygame.display.set_mode((800, 500))
pygame.display.set_caption("Spooky-Monster")
FUNDO = pygame.image.load("imagens/fundo.png")
FUNDO = pygame.transform.scale(FUNDO, (800, 500))

rodando = True
while rodando:
    #Tratando eventos
    for evento in pygame.event.get():
        if evento.type == pygame.MOUSEBUTTONDOWN:
            print("Você clicou!!")
        if evento.type == pygame.QUIT:
            rodando = False
    tela.blit(FUNDO,(0,0))

#Atualizando tela
    pygame.display.update()