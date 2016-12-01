from Model.Tabuleiro import *
class Jogo(object):

    def __init__(self, jogador1, jogador2, tabuleiro):
        self.jogador1 = jogador1
        self.jogador2 = jogador2
        self.tabuleiro = tabuleiro

    def novoJogo(self, jogador1, jogador2):
        self.init(jogador1, jogador2, Tabuleiro(8,8,jogador1))

    def salvarJogo(self, caminhoDoArquivo):
        return

    def carregarJogo(self, caminhoDoArquivo):
        return