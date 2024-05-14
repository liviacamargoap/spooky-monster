import pygame
import random

class Comida:

    def __init__(self,arquivo_imagem,largura_imagem,altura_imagem,x_inicial,y_inicial):
        self.imagem = pygame.image.load(arquivo_imagem)

        self.largura = largura_imagem
        self.altura = altura_imagem

        self.imagem = pygame.transform.scale(self.imagem,(self.largura,self.altura))

        self.pos_x = random.randint(1, 800)
        self.pos_y = y_inicial

        self.velocidade = random.randint(1, 6)

        self.mascara = pygame.mask.from_surface(self.imagem)
    

    def movimenta(self):
        self.pos_y = self.pos_y + self.velocidade
        if self.pos_y > + 500:
            self.pos_y = - 800
            self.velocidade = random.randint(2,2)
        self.pos_x = random.randint(1, 3)

    def desenhar(self, tela):
        tela.blit(self.imagem,(self.pos_x,self.pos_y)) 