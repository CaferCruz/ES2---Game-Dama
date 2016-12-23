#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Tabuleiro import *
from Jogador import *
from Jogo import *
from Peca import *


class Tests(object):

    """
        Caso em que vitoria ganho, não existe peças do adversário
    """
    def vitoria_branco(self):
        tabuleiro = Tabuleiro(8, 8)
        tabuleiro.esvaziar_lista()

        #Adiciona uma peça branca qualquer
        tabuleiro.addPeca(0, (0,0), 0)

        jogador1 = Jogador(tabuleiro.lista_das_brancas)
        jogador2 = Jogador(tabuleiro.lista_das_pretas)

        return Jogo(jogador1, jogador2, tabuleiro)

    """
        Caso em que vitoria ganho, não existe peças do adversário
    """
    def vitoria_preto(self):
        tabuleiro = Tabuleiro(8, 8)
        tabuleiro.esvaziar_lista()

        # Adiciona uma peça preta qualquer
        tabuleiro.addPeca(1, (0, 0), 0)

        jogador1 = Jogador(tabuleiro.lista_das_brancas)
        jogador2 = Jogador(tabuleiro.lista_das_pretas)

        return Jogo(jogador1, jogador2, tabuleiro)

    """
        Caso em que peça da origem está fora do tabuleiro
    """
    def peca_x_fora(self):
        tabuleiro = Tabuleiro(8,8)
        origem = (-1, 1)
        peca = Peca(0, origem, 0)
        destino = (2, 2)

        return [tabuleiro, peca, origem, destino]

    """
        Caso em que peça do destino está fora do tabuleiro
    """
    def peca_y_fora(self):
        tabuleiro = Tabuleiro(8, 8)
        origem = (1, 1)
        peca = Peca(0, origem, 0)
        destino = (-2, 2)

        return [tabuleiro, peca, origem, destino]

    """
        Caso em que peça existe no local passado
    """
    def peca_existe(self):
        tabuleiro = Tabuleiro(8, 8)
        origem = (1, 5)
        peca = Peca(0, origem, 0)
        destino = (0, 4)

        return [tabuleiro, peca, origem, destino]

    """
        Caso em que peça NÃO existe no local passado
    """
    def peca_nao_existe(self):
        tabuleiro = Tabuleiro(8, 8)
        origem = (0, 5)
        peca = Peca(0, origem, 0)
        destino = (0, 4)

        return [tabuleiro, peca, origem, destino]

    """
        Caso em que a posição de destino está vazia
    """
    def espaco_vazio(self):
        tabuleiro = Tabuleiro(8, 8)
        origem = (1, 5)
        peca = Peca(0, origem, 0)
        destino = (0, 4)

        return [tabuleiro, peca, origem, destino]

    """
        Caso em que a posição de destino está ocupado
    """
    def espaco_ocupado(self):
        tabuleiro = Tabuleiro(8, 8)
        origem = (1, 5)
        peca = Peca(0, origem, 0)
        destino = (0, 4)
        pecaPreta = Peca(1, destino, 0)
        tabuleiro.lista_das_pretas.append(pecaPreta)

        return [tabuleiro, peca, origem, destino]

    """
        Caso o jogador esteja com sua peça
    """
    def jogador_valido(self):
        tabuleiro = Tabuleiro(8, 8)
        origem = (1, 5)
        peca = Peca(0, origem, 0)
        destino = (0, 4)

        return [tabuleiro, peca, origem, destino]

    """
        Caso o jogador está tentando mover uma peça que não lhe pertence
    """
    def jogador_invalido(self):
        tabuleiro = Tabuleiro(8, 8)
        origem = (0, 2)
        peca = Peca(0, origem, 0)
        destino = (0, 4)

        return [tabuleiro, peca, origem, destino]

    """
        Caso o jogador está tentando mover uma peça que não lhe pertence
    """
    def jogada_obrigatoria(self):
        tabuleiro = Tabuleiro(8, 8)
        origem = (3, 6)
        peca = Peca(0, origem, 0)
        destino = (1, 4)

        tabuleiro.esvaziar_lista()
        #Adiciona uma peça para comer
        tabuleiro.addPeca(0, origem, 0)
        # Adiciona uma peça a ser comida
        tabuleiro.addPeca(1, (2, 5), 0)

        return [tabuleiro, peca, origem, destino]

    """
        Caso em que o jogador não possui uma lista de obrigações para comer
    """
    def passar_jogada(self):
        tabuleiro = Tabuleiro(8, 8)
        origem = (3, 6)
        peca = Peca(0, origem, 0)

        tabuleiro.esvaziar_lista()
        # Adiciona uma peça para comer
        tabuleiro.addPeca(0, origem, 0)
        destino = (2, 5)

        return [tabuleiro, peca, origem, destino]