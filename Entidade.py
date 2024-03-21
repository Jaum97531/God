import pygame

class Entidade() :
    def __init__(self, posX, posY, largura, altura, textura) :
        self.corpo = pygame.Rect(posX, posY, largura, altura)
        self.textura = pygame.image.load(textura)
        self.textura = pygame.transform.scale(self.textura, (largura, altura))  # Redimensiona a textura para o tamanho desejado
    
    def desenhar(self, tela) :
        tela.blit(self.textura, self.corpo)
    
    def execute(self) :
        pass