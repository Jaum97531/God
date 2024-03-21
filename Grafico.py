import pygame
import sys
pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class Grafico :
    instacia = None
   
    def __new__(cls) : 
        if cls.instacia is None :
            cls.instacia = super().__new__(cls)
        return cls.instacia

    def __init__(self):
        self.largura = 800
        self.altura = 600
        self.fonte = pygame.font.Font(None, 20)
        self.tela = pygame.display.set_mode((self.largura, self.altura))
        pygame.display.set_caption("GOD")
    
    def atualizar(self) :
        pygame.display.flip()
    
    def limpar(self) : 
        self.tela.fill(BLACK)
    
    def drawEntidade(self, entidade) : 
        entidade.draw(self.tela)
    
    def drawTexto(self, texto, posicao) :
        self.tela.blit(texto, posicao)
        
        
    