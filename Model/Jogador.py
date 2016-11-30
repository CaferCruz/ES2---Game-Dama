from Peca import *
class Jogador(object):


    def __init__(self, pecas):
        self.pecas = pecas

    def moverPecas(self, tabuleiro, peca, posDestino):
        if peca.cor == 0:

            for pecab in tabuleiro.lista_das_brancas:
                if(pecab.coordenadas == peca.coordenadas):
                    pecab.coordenadas = posDestino

        if peca.cor == 1:
            for pecap in tabuleiro.lista_das_pretas:
                if (pecap.coordenadas == peca.coordenadas):
                    pecap.coordenadas = posDestino




