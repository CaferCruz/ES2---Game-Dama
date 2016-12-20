#!/usr/bin/env python
from Regras import *

class Node(object):

    def __init__(self, tabuleiro, vez, regras):
        self.tabuleiro = tabuleiro
        self.vez = vez
        self.filhos = [] # Popular lista dos tabuleiros de acordo com as jogadas possiveis
        self.regras = regras
        self.valor = 0 # Calcular a avaliacao do tabuleiro


    def faz_filho(self):
        if self.vez == 0: #vez e branco
            branca_come_preta = self.regras.pedras_podem_comer(self.tabuleiro, 0)
            if len(branca_come_preta) > 0:
                print "Branco e obrigado a comer. "
                # So tabuleiro originados das comidas vao pra filhos
                numero_de_filhos = 0 # so pra debugar, isso tem que ser igual ao numero de filhos
                for peca in branca_come_preta:
                    origem = peca.coordenadas
                    for jogada in peca.jogadas_possiveis:
                        destino = peca.jogadas_possiveis
                        tabuleiro_temporario = self.tabuleiro
                        self.regras.mover(tabuleiro_temporario, peca.cor, [origem, destino], peca.tipo)
                        # total_mv = regras.mover(tabuleiro, corPeca, jogada, 0)
                        numero_de_filhos += 1
                        self.filhos.append(tabuleiro_temporario)
