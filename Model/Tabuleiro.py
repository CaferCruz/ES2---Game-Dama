# coding: utf-8

# Tabuleiro do jogo. Precisa de uma altura e uma largura para ser instanciado
from Peca import *
class Tabuleiro(object):
    PRETA = 1
    BRANCA = 0
    ND = -1

    def __init__(self, altura, largura, primeiroJogador):
        """
            Monta o tauleiro, profundidade eh estaticamente atribuida
        """
        # Define altura e largura do tabuleiro
        self.largura = largura
        self.altura = altura

        # Cria duas listas, cada uma contendo as pecas que cada jogador tem
        self.lista_das_pretas = []
        self.lista_das_brancas = []

        # Colocando as pecas nas posicoes iniciais
        for i in range(largura):
            self.lista_das_pretas.append(Peca(1,(i, i % 2),0),0)
            self.lista_das_brancas.append(Peca(0,(i, altura - (i % 2) - 1)),0)
            if (largura == 8) and (i == 0):
                self.lista_das_brancas.append(Peca(0,(i, 5),0))
                self.lista_das_brancas.append(Peca(0,(2, 5),0))
                self.lista_das_brancas.append(Peca(0,(4, 5),0))
                self.lista_das_brancas.append(Peca(0,(6, 5),0))
                self.lista_das_pretas.append(Peca(1,(i, 2),0))
                self.lista_das_pretas.append(Peca(1,(2, 2),0))
                self.lista_das_pretas.append(Peca(1,(4, 2),0))
                self.lista_das_pretas.append(Peca(1,(6, 2),0))
