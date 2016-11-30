from Peca import *
class Jogador(object):


    def __init__(self, pecas):
        self.pecas = pecas

    def moverPecas(self, tabuleiro, peca, posDestino):
        if peca.cor == 0:
            tabuleiro.lista_das_brancas.remove(peca)
            tabuleiro.lista_das_brancas.append(Peca(peca.cor, posDestino))
        if peca.cor == 1:
            tabuleiro.lista_das_pretas.remove(peca)
            tabuleiro.lista_das_pretas.append(Peca(peca.cor, posDestino))



