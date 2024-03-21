import Grafico
import pygame
import Lobby
import sys
pygame.init()

class Jogo :
    grafico = Grafico.Grafico()
    lobby = Lobby.Lobby()
      
    def __init__(self) : 
        self.loop_principal()
        
    def loop_principal(self) :
        while True :
            self.grafico.limpar()
            self.tratarEventos()
            self.lobby.execute()
            self.grafico.atualizar()
            
    def tratarEventos(self) :
        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                pygame.quit()
                sys.exit()
            elif (event.type == pygame.KEYDOWN) and self.lobby.digitar:
                if event.key == pygame.K_BACKSPACE:  # Se pressionar a tecla Backspace, apaga o último caractere
                    self.lobby.texto_digitado = self.lobby.texto_digitado[:-1]
                elif event.key == pygame.K_RETURN: # Se clicar enter ele envia o texto para o deus responder
                    self.lobby.gerar_resposta(self.lobby.texto_digitado)
                else:
                    self.lobby.texto_digitado += event.unicode
            elif event.type == pygame.MOUSEBUTTONDOWN :
                self.lobby.verifica_click()
        
            


