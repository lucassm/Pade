# -*- encoding: utf-8 -*-

from utils import display_message, set_ams, start_loop, config_loop
config_loop()
from agent import Agent
from messages import ACLMessage
from aid import AID
from protocols import FipaContractNetProtocol
from filters import Filter
from pickle import loads, dumps
from time import sleep

#===============================================================================
# Note, o que é necessário para criar um agente com comportamentos padronizados
# em protocolos?
# Primeiro, é preciso definir a classe protocolo
# Segundo é preciso associar esta classe protocolo como um comportamento do 
# agente
#===============================================================================

class ComportamentoAgenteLivraria(FipaContractNetProtocol):
    def __init__(self, agent):
        super(ComportamentoAgenteLivraria, self).__init__(agent, is_initiator=False)
    
    def handle_cfp(self, message):
        FipaContractNetProtocol.handle_cfp(self, message)
        display_message(self.agent.aid.name, 'Solicitação Recebida')
        
        pedido = loads(message.content)
        
        for book in self.agent.booksList:
            if book['title'] == pedido['title'] and book['author'] == pedido['author']:
                if book['qtd'] >= pedido['qtd']:
                    response = message.create_reply()
                    response.set_performative(ACLMessage.PROPOSE)
                    book['book store'] = self.agent.aid.name
                    response.set_content(dumps(book))
                    self.agent.send(response)
                else:
                    response = message.create_reply()
                    response.set_performative(ACLMessage.REJECT_PROPOSAL)
                    response.set_content('Requisição Recusada')
                    self.agent.send(response)
    
    def handle_accept_propose(self, message):
        FipaContractNetProtocol.handle_accept_propose(self, message)
        
        display_message(self.agent.aid.name, 'Proposta Aceita')
        
        response = message.create_reply()
        response.set_performative(ACLMessage.INFORM)
        response.set_content('Compra Autorizada')
        self.agent.send(response)
        
        
    def handle_reject_proposes(self, message):
        FipaContractNetProtocol.handle_reject_proposes(self, message)
        
        display_message(self.agent.aid.name, 'Proposta Recusada')

class AgenteLivraria(Agent):
    
    def __init__(self, aid, booksList):
        Agent.__init__(self, aid)
        
        self.booksList = booksList
        
        comportamento = ComportamentoAgenteLivraria(self)
        self.addBehaviour(comportamento)

if __name__ == '__main__':
    
    bookslist_Nobel = [{'title' : 'The Lord of the Rings', 'author' : 'J. R. R. Tolkien', 'qtd' : 10, 'how much is' : 63.50},
                         {'title' : 'Harry Potter', 'author' : 'J. K. Roling', 'qtd' : 10, 'how much is' : 35.70},
                         {'title' : 'Game of Thrones', 'author' : 'A. M. M. Martin', 'qtd' : 10, 'how much is' : 33.80}
                         ]
    
    bookStoresInfo = [(AID(name='Nobel@192.168.0.101:2001'), bookslist_Nobel)]
    
    pedido = {'title' : 'The Lord of the Rings', 'author' : 'J. R. R. Tolkien', 'qtd' : 5}
    
    agents = []
    
    nobel = AgenteLivraria(AID(name='Nobel'), bookslist_Nobel)
    nobel.set_ams('192.168.0.101', 8000)
    agents.append(nobel)
    
    start_loop(agents)