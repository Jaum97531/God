import Grafico
import pygame
import God
import time

class Lobby : 
    grafico = Grafico.Grafico()
    historico = []
    cont_mensagem = 0
    tamanho_mensagem = 0
    mensagem = ""
    texto_digitado = ""
    listaEntidades = []
    intervalo = 0.05
    tempo = time.time()
    digitar = False
    
    def __init__(self) :
        self.god = God.God(self.grafico.largura/2 - 150, self.grafico.altura/2 - 165, 300, 330)
        self.listaEntidades.append(self.god)
        
    def execute(self) :
        for entidade in self.listaEntidades :
            entidade.execute()
        
        self.exibir_texto()
        self.atualizar_resposta()
        self.desenhar()
    
    def desenhar(self) : 
        for it in self.listaEntidades :
            it.desenhar(self.grafico.tela)
    
    def verifica_click(self) :
        mouse_pos = pygame.mouse.get_pos()
        if self.god.corpo.collidepoint(mouse_pos) :
            self.digitar = not self.digitar        
            
    
    def gerar_resposta(self, pergunta) :
        self.mensagem = self.god.responder(pergunta)
        self.tamanho_mensagem = len(self.mensagem)
        self.cont_mensagem = 0
    
    def atualizar_resposta(self) : 
        cont = self.cont_mensagem
        mensagem = self.mensagem
        tamanho = self.tamanho_mensagem
        
        t_atual = time.time()
        if cont < tamanho and  t_atual - self.tempo >= self.intervalo:
            self.cont_mensagem += 1
            
            if cont % 100 == 0 :
                i = cont
                while mensagem[i] != ' ' and i < tamanho :
                    i += 1
                self.mensagem = self.mensagem[0:self.cont_mensagem] + "*" + self.mensagem[i:tamanho]
                
            self.tempo = t_atual

         
        texto = self.grafico.fonte.render(self.mensagem[0:self.cont_mensagem], True, Grafico.WHITE)
        posicao = texto.get_rect(center=(self.grafico.largura/2, self.grafico.altura - 100))
        self.grafico.drawTexto(texto, posicao)
        
    def exibir_texto(self) :
        texto = self.grafico.fonte.render(self.texto_digitado, True, Grafico.WHITE)
        posicao = texto.get_rect(center=(self.grafico.largura/2, 10))
        self.grafico.drawTexto(texto, posicao)
        
         