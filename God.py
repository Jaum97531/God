import Entidade
import gpt
import json
import requests

class God(Entidade.Entidade) :
    historico = []
    descricao = "Voce é um Deus que foi esquecido a muitos seculos, não sabe muito das novidades dos dias atuais, faz referencias a coisas que você viveu a muitos e muitos anos, e um pouco arrogante, é sarcastico, se irrita facil, mas também é muito sabio, as vezes você faz perguntas para o user, se não estiver com vontade nao responda as peguntas"
    consiencia = gpt.GPT()
    
    def __init__(self, posX, posY, largura, altura) :
        super().__init__(posX, posY, largura, altura, "god.png")
        self.load_historico()
        
    def load_historico(self) :
        with open('historico_mensagens.txt', 'r') as arquivo:
            conteudo = arquivo.read()
            if conteudo.strip():  # Verifica se a string não está vazia
                self.historico = json.loads(conteudo)
            else:
                self.historico = []
            
    def salvar_historico(self) : 
        with open('historico_mensagens.txt', 'w') as arquivo:
            arquivo.write(str(self.historico))        
    
    def responder(self, mensagem) :
        resposta = self.gerarResposta(mensagem)
        self.historico.append(resposta)
        return resposta["content"]
    
    def gerarResposta(self, mensagem) :
        self.historico.append({ "role": "system",  "content": self.descricao })
        self.historico.append({ "role": "user", "content": mensagem })
        
        body_mensagem = {
            "model" : self.consiencia.id_modelo,
            "messages" : self.historico ,
        }

        body_mensagem = json.dumps(body_mensagem)
        
        requisicao = requests.post(self.consiencia.link, headers=self.consiencia.headers, data=body_mensagem)
        requisicao = requisicao.json()
        
        resposta_chat = requisicao["choices"][0]["message"]
        return resposta_chat

    
    def desenhar(self, tela) :
        tela.blit(self.textura, self.corpo)
    