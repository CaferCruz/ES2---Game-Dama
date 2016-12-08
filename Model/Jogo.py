from Tabuleiro import *
from Jogador import *

class Jogo(object):

    def __init__(self, jogador1, jogador2, tabuleiro):
        self.jogador1 = jogador1
        self.jogador2 = jogador2
        self.tabuleiro = tabuleiro

