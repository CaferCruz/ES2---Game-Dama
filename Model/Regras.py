#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Peca import *
from Jogo import *
import os
import json
from Tabuleiro import *


class Regras(object):

    # Regra de empate definida pelo grupo. 20 rodadas(1 rodada = 1 jogada preta e 1 jogada branca) sem ninguem comer ninguem
    def empate(self, rodadasSemComer):
        if rodadasSemComer == 20:
            return True
        return False

    # Verifica se alguem venceu. Se preto venceu, retorna 1. Se branco venceu, retorna 0. Se ninguem venceu, retorna -1.
    def vitoria(self, tabuleiro):
        if len(tabuleiro.lista_das_brancas) == 0:
            return 1
        if len(tabuleiro.lista_das_pretas) == 0:
            return 0
        return -1

    # Verifica se a peca que esta sendo movida deve virar dama ou nao.
    def dentro_do_tabuleiro(self, coluna, linha):
        if (coluna < 0) or (coluna > 7) or (linha < 0) or (linha > 7):
            #print "coordenada: (coluna: ", coluna, ", linha: ", linha, ") nao esta dentro do tabuleiro."
            return False
        return True

    def exise_peca_em(self, tabuleiro, coordenada):
        """
        Retorna a peca se existente na coordenada passada
        Senao retorna None
        """
        for peca_branca in tabuleiro.lista_das_brancas:
            # print "*******************************"
            # print "pb_c: ",peca_branca.coordenadas
            # print "coordenada :",coordenada
            # peca_branca.printa_peca()
            # print "_______________________________"
            if peca_branca.coordenadas[0] == coordenada[0] and peca_branca.coordenadas[1] == coordenada[1]:
                return peca_branca
        for peca_preta in tabuleiro.lista_das_pretas:
            if peca_preta.coordenadas[0] == coordenada[0] and peca_preta.coordenadas[1] == coordenada[1]:
                return peca_preta
        return None



    def pedras_pretas_podem_comer(self, tabuleiro): #essa funcao e facilmente modularizavel ja que agora e possivel comer pra frente e pra tras
        """
        Retorna lista de pedras pretas que podem comer e
        atribui as movimentacoes as jogadas possiveis da peca
        se a lista for vazia nao existe movimento para comer
        """
        podem_comer = []
        for peca_preta in tabuleiro.lista_das_pretas:
            if peca_preta.tipo == 0:
                p_coluna = peca_preta.coordenadas[0]
                p_linha = peca_preta.coordenadas[1]
                if (self.dentro_do_tabuleiro(p_coluna + 1, p_linha + 1)) and (self.dentro_do_tabuleiro(p_coluna + 2, p_linha + 2)):  # baixo direita
                    peca_em_coordenada = self.exise_peca_em(tabuleiro, [p_coluna + 1, p_linha + 1])
                    if (peca_em_coordenada is not None) and (peca_em_coordenada.cor != peca_preta.cor):
                        if self.exise_peca_em(tabuleiro, [p_coluna + 2, p_linha + 2]) is None:
                            peca_preta.jogadas_possiveis.append([p_coluna + 2, p_linha + 2])
                            podem_comer.append(peca_preta)
                if (self.dentro_do_tabuleiro(p_coluna - 1, p_linha + 1)) and (self.dentro_do_tabuleiro(p_coluna - 2, p_linha + 2)):  # baixo esquerda
                    peca_em_coordenada = self.exise_peca_em(tabuleiro, [p_coluna - 1, p_linha + 1])
                    if (peca_em_coordenada is not None) and (peca_em_coordenada.cor != peca_preta.cor):
                        if self.exise_peca_em(tabuleiro, [p_coluna - 2, p_linha + 2]) is None:
                            peca_preta.jogadas_possiveis.append([p_coluna - 2, p_linha + 2])
                            podem_comer.append(peca_preta)
                if (self.dentro_do_tabuleiro(p_coluna + 1, p_linha - 1)) and (self.dentro_do_tabuleiro(p_coluna + 2, p_linha - 2)): # cima direita
                    peca_em_coordenada = self.exise_peca_em(tabuleiro, [p_coluna + 1, p_linha - 1])
                    if(peca_em_coordenada is not None) and (peca_em_coordenada.cor != peca_preta.cor):
                        if self.exise_peca_em(tabuleiro, [p_coluna + 2, p_linha - 2]) is None:
                            peca_preta.jogadas_possiveis.append([p_coluna + 2, p_linha - 2])
                            podem_comer.append(peca_preta)
                if (self.dentro_do_tabuleiro(p_coluna - 1, p_linha - 1)) and (self.dentro_do_tabuleiro(p_coluna - 2, p_linha - 2)): # cima esquerda
                    peca_em_coordenada = self.exise_peca_em(tabuleiro, [p_coluna - 1, p_linha - 1])
                    if (peca_em_coordenada is not None) and (peca_em_coordenada.cor != peca_preta.cor):
                        if self.exise_peca_em(tabuleiro, [p_coluna - 2, p_linha -2]) is None:
                            peca_preta.jogadas_possiveis.append([p_coluna - 2, p_linha - 2])
                            podem_comer.append(peca_preta)
        if len(podem_comer) > 0: print "pedras pretas podem comer"
        return podem_comer

    def virarDama(self, peca, altura):
        if peca.tipo == 1:
            return False
        if peca.coordenadas[1] == 0 and peca.cor == 0:
            return True
        if peca.coordenadas[1] == altura and peca.cor == 1:
            return True
        return False

    """
        Verifica se peça pertence ao jogador da vez.
    """
    def pecas_validas(self, tabuleiro, jogada, corPeca):
        origem = (int(jogada[0][1]), ord(jogada[0][0]) - 97)

        existe = tabuleiro.get_coodenada(origem)
        if existe is not None:
            return True
        return False

    """
        Atualiza coordenada, quando realizado um movimento.
    """
    def atualiza_coordenada(self, peca, destino, tabuleiro):
        p = tabuleiro.get_coodenada(peca.coordenadas)
        if p is not None and p.cor == peca.cor:
            p.coordenadas = destino
            return True
        return False


    """
        Movimenta peça, se a peça for da lista de depças do jogador
    """
    def mover(self, tabuleiro, cor, jogada, tipoPeca):
        origem = (int(jogada[0][1]), ord(jogada[0][0]) - 97)
        peca = Peca(cor, origem, tipoPeca)
        destino = (int(jogada[1][1]), ord(jogada[1][0]) - 97)
        self.atualiza_coordenada(peca, destino, tabuleiro)

        #Essa parte ainda será refatorada
        if cor == 0:
            self.comerPreta(tabuleiro, peca, origem, destino)
            jogada = (peca, destino)
            lista_de_jogadas_comendo = self.pedras_brancas_podem_comer(tabuleiro)
            if lista_de_jogadas_comendo == [] :
                print "brancas pode mover sem comer"
            else:
                print "brancas tem que mover comendo senao nao pode mover"
                for b in lista_de_jogadas_comendo:
                    if b.coordenadas[0] == origem[0] and b.coordenadas[1] == origem[1] and b.jogadas_possiveis != []:
                        for j in b.jogadas_possiveis:
                            if j == destino:
                                print origem, ", ", destino, "essa jogada pode."
                            else:
                                print destino," nao esta nas jogadas possiveis de ", origem
                    else:
                        print "essa peca nao pode comer, selecione uma peca que possa"
            return jogada
        else:
            self.comerBranca(tabuleiro, peca, origem, destino)
            jogada = (peca, destino)

            if self.pedras_pretas_podem_comer(tabuleiro) == [] :
                print "pretas pode mover sem comer"
            else:
                print "pretas tem que mover comendo senao nao pode mover. Numero de pecas que podem comer: ", len(self.pedras_pretas_podem_comer(tabuleiro))

            return jogada
        return None

    """
        Verificar antes se jogador eh obrigado a comer
    """
    def valida_mover(self, tabuleiro, peca, origem, destino):
        peca_em_coordenada = self.exise_peca_em(tabuleiro, peca.coordenadas)
        if peca.tipo == 1:
            self.valida_movimento_dama(tabuleiro, peca, origem, destino)
        if self.dentro_do_tabuleiro(origem[0], origem[1]) and self.dentro_do_tabuleiro(destino[0], destino[1]): #se origem e destino esta dentro do tabuleiro
            if peca_em_coordenada is not None: # se tem alguma peca
                if peca.cor == peca_em_coordenada.cor: #se a peca que esta na casa eh da cor da peca que foi passada
                    if peca.cor == 0:
                        if self.valida_movimento_peca_branca(tabuleiro, peca, origem, destino):
                            print "Pode mover peca ", peca.coordenadas #CHAMA A FUNCAO DE MOVER AGORA!!!!
                    elif peca.cor == 1:
                        if self.valida_movimento_peca_preta(tabuleiro, peca, origem, destino):
                            print "Pode mover peca ", peca.coordenadas #CHAMA A FUNCAO DE MOVER AGORA!!!!
                else:
                    print "Cor da peca encontrada em origem diferente da cor da peca recebida como parametro."
            else:
                print "Nao existe nenhuma peca no local passado como origem."
        else:
            print "Coordenada passada esta fora do tabuleiro."

    def valida_movimento_dama(self, tabuleiro, peca, origem, destino):
        d_coluna = peca.coordenadas[0]
        d_linha = peca.coordenadas[1]
        i = 1
        # verificar nordeste se tem uma casa livre entre origem e destino nessa direcao antes de encontrar uma peca branca
        # se a coluna destino e maior que a origem e linha destino menor que linha origem movimento nordeste
        if (origem[0] < destino[0]) and (origem[1] > destino[1]):
            peca_em_coordenada = self.exise_peca_em(tabuleiro, [d_coluna + i, d_linha - i])
            if peca_em_coordenada is None: # se tem pelo menos uma casa livre a nordeste, conte quantas livres casas a nordeste tem
                while peca_em_coordenada is None:
                    i += 1
                    peca_em_coordenada = self.exise_peca_em(tabuleiro, [d_coluna + i, d_linha - i])
                    if not self.dentro_do_tabuleiro(peca_em_coordenada[0], peca_em_coordenada[1]): break #IF NOT PECA DENTRO DO TABULEIRO BREAK
                print "Dama pode andar ", i, " colunas e ", i, " linhas."
                if (destino[0] - origem[0] > 0) and (destino[0] - origem[0] <= i) and (origem[1] - destino[1] > 0) and (origem[1] - destino[1] <= i):
                    print "Movimento validado da dama: ", peca.coordenadas, " para ", destino, "andando ", i, " casas a nordeste."
                    return True
                else: print "Dama deve andar no minimo 1 casa a nordeste e no maximo ", i, " casas a nordeste."
            else:
                print "Dama nao tem para onde andar, ", i - 1, " casas vazias a nordeste."
        # se a coluna destino e maior que a origem e linha destino menor que linha origem movimento noroeste
        if (origem[0] > destino[0]) and (origem[1] > destino [1]):
            peca_em_coordenada = self.exise_peca_em(tabuleiro, [d_coluna - i, d_linha - i])
            if peca_em_coordenada is None: # se tem pelo menos uma casa livre a noroeste, conte quantas casas livres a noroeste tem
                while peca_em_coordenada is None:
                    i += 1
                    peca_em_coordenada = self.exise_peca_em(tabuleiro, [d_coluna - i, d_linha - i])
                    if not self.dentro_do_tabuleiro(peca_em_coordenada[0], peca_em_coordenada[1]): break # IF NOT PECA DENTRO DO TABULEIRO BREAK
                print "Dama pode andar ", i, " colunas e ", i, " linhas."
                if (origem[0] - destino[0] > 0) and (origem[0] - destino[0] <= i) and (origem[1] - destino[1] > 0) and (origem[1] - destino[1] <= i):
                    print "Movimento validado da dama: ", peca.coordenadas, " para ", destino, "andando ", i, " casas a noroeste."
                    return True
                else: print "Dama deve andar no minimo 1 casa a noroeste e no maximo ", i, " casas a noroeste."
            else:
                print "Dama nao tem para onde andar, ", i - 1, " casas vazias a noroeste."
        # se a coluna destino e maior que a origem e linha destino maior que linha origem movimento sudeste
        if (destino[0] > origem[0]) and (origem[1] > destino [1]):
            peca_em_coordenada = self.exise_peca_em(tabuleiro, [d_coluna + i, d_linha + i])
            if peca_em_coordenada is None: # se tem pelo menos uma casa livre a sudeste, conte quantas casas livres a sudeste tem
                while peca_em_coordenada is None:
                    i += 1
                    peca_em_coordenada = self.exise_peca_em(tabuleiro, [d_coluna + i, d_linha + i])
                    if not self.dentro_do_tabuleiro(peca_em_coordenada[0], peca_em_coordenada[1]): break # IF NOT PECA DENTRO DO TABULEIRO BREAK
                print "Dama pode andar ", i, " colunas e ", i, " linhas."
                if (destino[0] - origem[0] > 0) and (destino[0] - origem[0] <= i) and (destino[1] - origem[1] > 0) and (destino[1] - origem[1] <= i):
                    print "Movimento validado da dama: ", peca.coordenadas, " para ", destino, "andando ", i, " casas a sudeste."
                    return True
                else: print "Dama deve andar no minimo 1 casa a sudeste e no maximo ", i, " casas a sudeste."
            else:
                print "Dama nao tem para onde andar, ", i - 1, " casas vazias a sudeste."
        # se a coluna destino e menor que a origem e a linha destino maior que linha origem movimento sudoeste
        if (destino[0] < origem[0]) and (origem[1] < origem[0]):
            peca_em_coordenada = self.exise_peca_em(tabuleiro, [d_coluna - i, d_linha + i])
            if peca_em_coordenada is None: # se tem pelo menos uma casa livre a sudoeste, conta quantas casas livres a sudoeste tem
                while peca_em_coordenada is None:
                    i += 1
                    peca_em_coordenada = self.exise_peca_em(tabuleiro, [d_coluna - i, d_linha + i])
                    if not self.dentro_do_tabuleiro(peca_em_coordenada[0], peca_em_coordenada[1]): break # IF NOT PECA DENTRO DO TABULEIRO BREAK
                print "Dama pode andar ", i, " colunas e ", i, " linhas."
                if (origem[0] - destino[0] > 0) and (origem[0] - destino[0] <= i) and (destino[1] - origem[1] > 0) and (destino[1] - origem[1] <= i):
                    print "Movimento validado da dama: ", peca.coordenadas, " para ", destino, "andando ", i, " casas a sudoeste."
                    return True
                else: print "Dama deve andar no minimo 1 casa a sudoeste e no maximo ", i, " casas a sudoeste"
            else:
                print "Dama nao tem para onde andar, ", i-1, " casas vazias a sudoeste."

    def valida_movimento_peca_branca(self, tabuleiro, peca, origem, destino):
        if peca.tipo == 0: #peca e pedra
            #verifica se e pra cima direita
            if (origem[0] + 1 == destino[0]) and (origem[1] - 1 == destino[1]):
                return True
            # verifica se e pra cima esquerda
            if (origem[0] - 1 == destino[0]) and (origem[1] - 1 == destino[1]):
                return True
            else:
                print "Peca ", peca.coordenadas," e pedra entao pode se mover apenas uma casa para nordeste (cima direita) ou noroeste (cima esquerda)."
                return False
        if peca.tipo == 1: #peca e dama
            if self.valida_movimento_dama(self, tabuleiro, peca, origem, destino):
                print "Pode mover dama branca: ", peca.coordenadas #chama move dama de origem pra destino

    def valida_movimento_peca_preta(self, tabuleiro, peca, origem, destino):
        if peca.tipo == 0: #peca e pedra
            #verifica se e pra baixo direita
            if (origem[0] + 1 == destino[0]) and (origem[1] + 1 == destino[1]):
                return True
            #verifica se e pra baixo esquerda
            if (origem[0] - 1 == destino[0]) and (origem[1] + 1 == destino[1]):
                return True
            else:
                print "Peca ", peca.coordenadas, " e pedra entao pode se mover apenas uma casa para sudeste (baixo direita) ou sudoeste (baixo esquerda)."
                return False
        if peca.tipo == 1: #peca e dama
            if self.valida_movimento_dama(self, tabuleiro, peca, origem, destino):
                print "Pode mover dama preta: ", peca.coordenadas #chama move dama de origem pra destino
                #chama move dama de origem pra destino

    """
        Retorna lista de pedras brancas que podem comer e
        atribui as movimentacoes as jogadas possiveis da peca
        se a lista for vazia nao existe movimento para comer
    """
    def pedras_brancas_podem_comer(self, tabuleiro): #essa funcao e facilmente modularizavel ja que agora e possivel comer pra frente e pra tras
        podem_comer = []
        for peca_branca in tabuleiro.lista_das_brancas:
            if peca_branca.tipo == 0:
                p_coluna = peca_branca.coordenadas[0]
                p_linha = peca_branca.coordenadas[1]
                #print "analisando peca: ",peca_branca.coordenadas
                # print "coordenadas a 1 lado",p_coluna+1," , ",p_linha+1, " e a 2 lado ", p_coluna + 2," , ",p_linha + 2," dentro do tabueiro?"
                # print "existe peca em 1 lado: ",self.exise_peca_em(tabuleiro, [p_coluna + 1, p_linha - 1])
                # print "existe peca em 2 lado: ",self.exise_peca_em(tabuleiro, [p_coluna + 2, p_linha - 2])
                if (self.dentro_do_tabuleiro(p_coluna + 1, p_linha + 1)) and (self.dentro_do_tabuleiro(p_coluna + 2, p_linha + 2)):  # baixo direita
                    peca_em_coordenada = self.exise_peca_em(tabuleiro, [p_coluna + 1, p_linha + 1])
                    if (peca_em_coordenada is not None) and (peca_em_coordenada.cor != peca_branca.cor):
                        if self.exise_peca_em(tabuleiro, [p_coluna + 2, p_linha + 2]) is None:
                            print "Pode comer em ", p_coluna + 2, ", ",p_linha + 2
                            peca_branca.jogadas_possiveis.append([p_coluna + 2, p_linha + 2])
                            podem_comer.append(peca_branca)
                if (self.dentro_do_tabuleiro(p_coluna - 1, p_linha + 1)) and (self.dentro_do_tabuleiro(p_coluna - 2, p_linha + 2)):  # baixo esquerda
                    peca_em_coordenada = self.exise_peca_em(tabuleiro, [p_coluna - 1, p_linha + 1])
                    if (peca_em_coordenada is not None) and (peca_em_coordenada.cor != peca_branca.cor):
                        if self.exise_peca_em(tabuleiro, [p_coluna - 2, p_linha + 2]) is None:
                            peca_branca.jogadas_possiveis.append([p_coluna - 2, p_linha + 2])
                            podem_comer.append(peca_branca)
                            print "Pode comer em ", p_coluna - 2, ", ",p_linha + 2
                if (self.dentro_do_tabuleiro(p_coluna - 1, p_linha - 1)) and (self.dentro_do_tabuleiro(p_coluna - 2, p_linha - 2)):  # cima esquerda
                    peca_em_coordenada = self.exise_peca_em(tabuleiro, [p_coluna - 1, p_linha - 1])
                    if (peca_em_coordenada is not None) and (peca_em_coordenada.cor != peca_branca.cor):
                        if self.exise_peca_em(tabuleiro, [p_coluna - 2, p_linha - 2]) is None:
                            print "Pode comer em ", p_coluna - 2, "," ,p_linha - 2
                            peca_branca.jogadas_possiveis.append([p_coluna - 2, p_linha - 2])
                            podem_comer.append(peca_branca)
                if (self.dentro_do_tabuleiro(p_coluna + 1, p_linha - 1)) and (self.dentro_do_tabuleiro(p_coluna + 2, p_linha - 2)):  # cima direita
                    peca_em_coordenada = self.exise_peca_em(tabuleiro, [p_coluna + 1, p_linha - 1])
                    if (peca_em_coordenada is not None) and (peca_em_coordenada.cor != peca_branca.cor):
                        #print"peca_em_coordenada ",peca_em_coordenada.coordenadas," eh ", peca_em_coordenada.cor," = peca_branca em ",peca_branca.coordenadas," eh ", peca_branca.cor
                        if self.exise_peca_em(tabuleiro, [p_coluna + 2, p_linha - 2]) is None:
                            print "Pode comer em ",p_coluna+2, ", ",p_linha-2
                            peca_branca.jogadas_possiveis.append([p_coluna + 2, p_linha - 2])
                            podem_comer.append(peca_branca)
        if len(podem_comer) > 0: print "pedras brancas podem comer"
        return podem_comer


    def damas_podem_comer(self, tabuleiro, peca): # passar a peca serve apenas para representar de quem e a vez atual
        podem_comer = []
        lista_pecas_adversario = []
        lista_minhas_pecas = []
        coordenada_dama = []
        if peca.cor == 0: # se a dama e branca
            lista_minhas_pecas = tabuleiro.lista_das_brancas
            lista_pecas_adversario = tabuleiro.lista_das_pretas
        elif peca.cor == 1: # se a dama e preta
            lista_minhas_pecas = tabuleiro.lista_das_pretas
            lista_pecas_adversario = tabuleiro.lista_das_brancas
        for minha_peca in lista_minhas_pecas:
            if minha_peca.tipo == 1:
                coordenada_dama.append(minha_peca.coordenadas)
        if len(coordenada_dama) == 0:
            return False # se nao tem dama, dama nao pode comer, duh.
        for dama in coordenada_dama:
            # conta quantas casas livres tem em cada diagonal
            i = 1
            d_coluna = peca.coordenadas[0]
            d_linha = peca.coordenadas[1]

            while self.exise_peca_em(tabuleiro, [d_coluna + i, d_linha - i]) is None: #nordeste
                if self.dentro_do_tabuleiro(d_coluna + i, d_linha - i):
                    i += 1

                else:
                    print "Saiu do tabuleiro"
                    encontrou_adversario = False
                    break
            print i," casas livres a nordeste."
            # se encontrar uma peca verifica se e peca do adversario
            # se for do adversario verifica se existe uma casa livre apos essa peca
            # se existir entao adicione esse movimento a    podem_comer
            # movimento na sudoeste

    def comerPreta(self, tabuleiro, peca, origem, destino):
        y = 0
        if (origem[0] < destino[0]):
            for l in range(origem[0] + 1, destino[0] + 1):
                y = y + 1
                coord = (l, origem[1] - y)
                for cod in tabuleiro.lista_das_pretas:
                    if cod.coordenadas == coord:
                        tabuleiro.removePreta(cod)
        else:
            for l in range(origem[0] - 1, destino[0] -1, -1):
                print(origem[0] - 1, destino[0] -1)
            print(origem[0], origem[1])
            for l in range(origem[0] - 1, destino[0] - 1, -1):
                print(origem[0] - 1, destino[0] - 1)
                y = y - 1
                coord = (l, origem[1] + y)
                for cod in tabuleiro.lista_das_pretas:
                    if cod.coordenadas == coord:
                        tabuleiro.removePreta(cod)

    def comerBranca(self, tabuleiro, peca, origem, destino):
        y = 0
        print('origem:', origem[0], origem[1])
        if (origem[0] > destino[0]):
            for l in range(origem[0] - 1, destino[0] - 1, -1):
                y = y + 1
                coord = (l, origem[1] + y)
                print(coord)
                for cod in tabuleiro.lista_das_brancas:
                    if cod.coordenadas == coord:
                        tabuleiro.removeBranca(cod)
        else:
            for l in range(origem[0] + 1, destino[0] + 1):
                y = y + 1
                coord = (l, origem[1] + y)
                print(coord)
                for cod in tabuleiro.lista_das_brancas:
                    if cod.coordenadas == coord:
                        tabuleiro.removeBranca(cod)


    def novoJogo(self):
        largura = 8
        altura = 8

        tabuleiro = Tabuleiro(largura, altura)
        jogador1 = Jogador(tabuleiro.lista_das_brancas)
        jogador2 = Jogador(tabuleiro.lista_das_pretas)

        return Jogo(jogador1, jogador2, tabuleiro)

    def salvarJogo(self, tabuleiro, nomeSave):
        caminho = "../save/" + nomeSave
        dados_json = {}

        dados_json["altura"] = 8
        dados_json["largura"] = 8
        dados_json["branco_peca"] = []
        dados_json["branco_dama"] = []
        dados_json["preto_peca"] = []
        dados_json["preto_dama"] = []

        for b in tabuleiro.lista_das_brancas:
            if b.tipo :
                dados_json["branco_dama"].append(b.coordenadas)
            else:
                dados_json["branco_peca"].append(b.coordenadas)

        for b in tabuleiro.lista_das_pretas:
            if b.tipo :
                dados_json["preto_dama"].append(b.coordenadas)
            else:
                dados_json["preto_peca"].append(b.coordenadas)

        with open(caminho, 'w') as infile:
            json.dump(dados_json, infile)
        infile.close()

    def carregarJogo(self, nomeSave):
        caminho = "../save/" + nomeSave

        outfile = open(caminho, 'r')
        out = outfile.readline()
        data = json.loads(out)

        tabuleiro = Tabuleiro(data['largura'], data['altura'])
        tabuleiro.esvaziar_lista()
        for b in data['branco_peca']:
            tabuleiro.addPeca(0, b, 0)

        for b in data['branco_dama']:
            tabuleiro.addPeca(0, b, 1)

        for p in data['preto_peca']:
            tabuleiro.addPeca(1, p, 0)

        for p in data['preto_dama']:
            tabuleiro.addPeca(1, p, 1)

        jogador1 = Jogador(tabuleiro.lista_das_brancas)
        jogador2 = Jogador(tabuleiro.lista_das_pretas)

        return Jogo(jogador1, jogador2, tabuleiro)
