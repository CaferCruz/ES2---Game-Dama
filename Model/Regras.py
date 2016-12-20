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

    """
        Retorna a peca se existente na coordenada passada
        Senao retorna None
    """
    def existe_peca_em(self, tabuleiro, coordenada):
        for peca_branca in tabuleiro.lista_das_brancas:
            if peca_branca.coordenadas == (coordenada[0], coordenada[1]):
                return peca_branca
        for peca_preta in tabuleiro.lista_das_pretas:
            if peca_preta.coordenadas == (coordenada[0], coordenada[1]):
                return peca_preta
        return None

    """
        Função usada para validar no front-end.
        Verifica todas as validações em valida_mover e se existe comer obrigatorio, se exitir é preciso estar na lista
        de obrigatorios.
    """
    def validador(self, tabuleiro, peca, origem, destino):
        regra_mover = self.valida_mover(tabuleiro, peca, origem, destino)
        if regra_mover:
            lista_mv_obg = self.pedras_podem_comer(tabuleiro, peca.cor)
            mv_obrigatorio = self.mover_obrigatorio(tabuleiro, origem, destino, lista_mv_obg)
            if not lista_mv_obg or mv_obrigatorio:
                return True
        return False

    """
        Retorna lista de pedras pretas que podem comer e
        atribui as movimentacoes as jogadas possiveis da peca
        se a lista for vazia nao existe movimento para comer
    """
    def pedras_podem_comer(self, tabuleiro, corJogada): #essa funcao e facilmente modularizavel ja que agora e possivel comer pra frente e pra tras
        podem_comer = []
        if corJogada:
            print("Verificar jogada para Pretos comer.")
            for peca_preta in tabuleiro.lista_das_pretas:
                if peca_preta.tipo == 0:
                    p_coluna = peca_preta.coordenadas[0]
                    p_linha = peca_preta.coordenadas[1]
                    if (self.dentro_do_tabuleiro(p_coluna + 1, p_linha + 1)) and (self.dentro_do_tabuleiro(p_coluna + 2, p_linha + 2)):  # baixo direita
                        peca_em_coordenada = self.existe_peca_em(tabuleiro, [p_coluna + 1, p_linha + 1])
                        #print("peca_em_coordenada: ", peca_em_coordenada, [p_coluna + 1, p_linha + 1])
                        if (peca_em_coordenada is not None) and (peca_em_coordenada.cor != peca_preta.cor):
                            if self.existe_peca_em(tabuleiro, [p_coluna + 2, p_linha + 2]) is None:
                                #print("1", [p_coluna + 2, p_linha + 2])
                                peca_preta.jogadas_possiveis.append((p_coluna + 2, p_linha + 2))
                                podem_comer.append(peca_preta)
                    if (self.dentro_do_tabuleiro(p_coluna - 1, p_linha + 1)) and (self.dentro_do_tabuleiro(p_coluna - 2, p_linha + 2)):  # baixo esquerda
                        peca_em_coordenada = self.existe_peca_em(tabuleiro, [p_coluna - 1, p_linha + 1])
                        #print("peca_em_coordenada: ", peca_em_coordenada, [p_coluna - 1, p_linha + 1])
                        if (peca_em_coordenada is not None) and (peca_em_coordenada.cor != peca_preta.cor):
                            if self.existe_peca_em(tabuleiro, [p_coluna - 2, p_linha + 2]) is None:
                                #print("2", (p_coluna + 1 , p_linha - 1 ))
                                peca_preta.jogadas_possiveis.append((p_coluna - 2, p_linha + 2))
                                podem_comer.append(peca_preta)
                    if (self.dentro_do_tabuleiro(p_coluna + 1, p_linha - 1)) and (self.dentro_do_tabuleiro(p_coluna + 2, p_linha - 2)): # cima direita
                        peca_em_coordenada = self.existe_peca_em(tabuleiro, [p_coluna + 1, p_linha - 1])
                        #print("peca_em_coordenada: ", peca_em_coordenada, [p_coluna + 1, p_linha - 1])
                        if(peca_em_coordenada is not None) and (peca_em_coordenada.cor != peca_preta.cor):
                            if self.existe_peca_em(tabuleiro, [p_coluna + 2, p_linha - 2]) is None:
                                #print("3",[p_coluna + 2, p_linha - 2])
                                peca_preta.jogadas_possiveis.append((p_coluna + 2, p_linha - 2))
                                podem_comer.append(peca_preta)
                    if (self.dentro_do_tabuleiro(p_coluna - 1, p_linha - 1)) and (self.dentro_do_tabuleiro(p_coluna - 2, p_linha - 2)): # cima esquerda
                        peca_em_coordenada = self.existe_peca_em(tabuleiro, [p_coluna - 1, p_linha - 1])
                        #print("peca_em_coordenada: ", peca_em_coordenada, [p_coluna - 1, p_linha - 1])
                        if (peca_em_coordenada is not None) and (peca_em_coordenada.cor != peca_preta.cor):
                            if self.existe_peca_em(tabuleiro, [p_coluna - 2, p_linha -2]) is None:
                                #print("4", [p_coluna + 1, p_linha + 1])
                                peca_preta.jogadas_possiveis.append((p_coluna - 2, p_linha - 2))
                                podem_comer.append(peca_preta)
                else:
                    damas = self.damas_podem_comer(tabuleiro, peca_preta)
                    podem_comer = podem_comer + damas

        else:
            print("Verificar jogada para branco comer.")
            for peca in tabuleiro.lista_das_brancas:
                if peca.tipo == 0:
                    p_coluna = peca.coordenadas[0]
                    p_linha = peca.coordenadas[1]
                    if self.dentro_do_tabuleiro(p_coluna + 2, p_linha + 2):  # baixo direita
                        peca_em_coordenada = self.existe_peca_em(tabuleiro, [p_coluna + 1, p_linha + 1])
                        # print("peca_em_coordenada: ", peca_em_coordenada, [p_coluna + 1, p_linha + 1])
                        if (peca_em_coordenada is not None) and (peca_em_coordenada.cor != peca.cor):
                            if self.existe_peca_em(tabuleiro, [p_coluna + 2, p_linha + 2]) is None:
                                #print("1", [p_coluna + 2, p_linha + 2])
                                peca.jogadas_possiveis.append((p_coluna + 2, p_linha + 2))
                                podem_comer.append(peca)
                    if self.dentro_do_tabuleiro(p_coluna - 2, p_linha + 2):  # baixo esquerda
                        peca_em_coordenada = self.existe_peca_em(tabuleiro, [p_coluna - 1, p_linha + 1])
                        # print("peca_em_coordenada: ", peca_em_coordenada, [p_coluna - 1, p_linha + 1])
                        if (peca_em_coordenada is not None) and (peca_em_coordenada.cor != peca.cor):
                            if self.existe_peca_em(tabuleiro, [p_coluna - 2, p_linha + 2]) is None:
                                #print("2", (p_coluna + 1, p_linha - 1))
                                peca.jogadas_possiveis.append((p_coluna - 2, p_linha + 2))
                                podem_comer.append(peca)
                    if self.dentro_do_tabuleiro(p_coluna + 2, p_linha - 2):  # cima direita
                        peca_em_coordenada = self.existe_peca_em(tabuleiro, [p_coluna + 1, p_linha - 1])
                        # print("peca_em_coordenada: ", peca_em_coordenada, [p_coluna + 1, p_linha - 1])
                        if (peca_em_coordenada is not None) and (peca_em_coordenada.cor != peca.cor):
                            if self.existe_peca_em(tabuleiro, [p_coluna + 2, p_linha - 2]) is None:
                                #print("3", [p_coluna + 2, p_linha - 2])
                                peca.jogadas_possiveis.append((p_coluna + 2, p_linha - 2))
                                podem_comer.append(peca)
                    if self.dentro_do_tabuleiro(p_coluna - 2, p_linha - 2):  # cima esquerda
                        peca_em_coordenada = self.existe_peca_em(tabuleiro, [p_coluna - 1, p_linha - 1])
                        # print("peca_em_coordenada: ", peca_em_coordenada, [p_coluna - 1, p_linha - 1])
                        if (peca_em_coordenada is not None) and (peca_em_coordenada.cor != peca.cor):
                            if self.existe_peca_em(tabuleiro, [p_coluna - 2, p_linha - 2]) is None:
                                #print("4", [p_coluna + 1, p_linha + 1])
                                peca.jogadas_possiveis.append((p_coluna - 2, p_linha - 2))
                                podem_comer.append(peca)
                else: #se nao e do tipo 0 entao e dama, e ai concatena com a lista gerada por damas podem comer
                    damas = self.damas_podem_comer(tabuleiro, peca)
                    podem_comer = podem_comer + damas

        return podem_comer


    def virarDama(self, peca):
        if peca.tipo == 0:
            if peca.coordenadas[1] == 0 and peca.cor == 0:
                peca.tipo = 1
                return True
            if peca.coordenadas[1] == 7 and peca.cor == 1:
                peca.tipo = 1
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
            self.virarDama(peca)
            return p
        return None

    def capsula_atualiza(self, peca, destino, tabuleiro):
        atualiza_coordenada(self, peca, destino, tabuleiro)
        return tabuleiro


    """
        Movimenta peça, se a peça for da lista de depças do jogador
    """
    def mover(self, tabuleiro, cor, jogada):
        origem = (int(jogada[0][1]), ord(jogada[0][0]) - 97)
        peca = self.existe_peca_em(tabuleiro, origem)
        destino = (int(jogada[1][1]), ord(jogada[1][0]) - 97)

        obgComer = self.valida_mover(tabuleiro, peca, origem, destino)

        if obgComer:
            peca = self.atualiza_coordenada(peca, destino, tabuleiro)# Move peça

            if cor:
                comer = self.comerBranca(tabuleiro, peca, origem, destino)  # Come peça branca
            else:
                comer = self.comerPreta(tabuleiro, peca, origem, destino) # Come peças pretas

            lista_mv_obg = self.pedras_podem_comer(tabuleiro, cor)
            for m in lista_mv_obg:
                print("Obrigatorio comer: ", m)
            if lista_mv_obg and comer:
                print(">>>>>>>Ainda existe jogadas para você.<<<<<<<<")
                return True
        return False


    """
        Verifica se tentativa de movimento é dos casos obrigatórios, senão, obriga apenas determinados movimentos.
        A verificação é feita apartir das coordenadas da lista de obrigatórias, se existir uma peça na posição e for diferente da cor da jogada da vez
        é obrigatorio comer.
    """
    def mover_obrigatorio(self, tabuleiro, origem, destino, lista_obrigatoria):
        for o in lista_obrigatoria:
            for d in o.jogadas_possiveis:
                if o.coordenadas == origem and d == destino:
                    return True
        return False

    """
        Verificar antes se jogador eh obrigado a comer
    """
    def valida_mover(self, tabuleiro, peca, origem, destino):  # Verificar antes se jogador eh obrigado a comer, se ela for comer nem chame essa funcao
        peca_em_coordenada = self.existe_peca_em(tabuleiro, peca.coordenadas)
        if self.dentro_do_tabuleiro(origem[0], origem[1]) and self.dentro_do_tabuleiro(destino[0], destino[1]):  # se origem e destino esta dentro do tabuleiro
            if peca_em_coordenada is not None: # se tem alguma peca na origem
                peca_destino = self.existe_peca_em(tabuleiro, destino)
                if peca_destino is None: # O espaço precisa estar vazio.
                    if peca.cor == peca_em_coordenada.cor: #se a peca que esta na casa eh da cor da peca que foi passada
                        if peca.tipo == 1:
                            resp = self.valida_caminho_dama(tabuleiro,peca, origem, destino)
                            return resp
                        else:
                            if peca.cor == 0:
                                if self.valida_movimento_peca_branca(tabuleiro, peca, origem, destino) or \
                                        self.valida_movimento_comer(tabuleiro, peca, origem, destino):
                                    print "Pode mover peca ", peca.coordenadas
                                    return True
                            elif peca.cor == 1:
                                if self.valida_movimento_peca_preta(tabuleiro, peca, origem, destino) or \
                                        self.valida_movimento_comer(tabuleiro, peca, origem, destino):
                                    print "Pode mover peca ", peca.coordenadas
                                    return True
                    else:
                        print "Cor da peca encontrada em origem diferente da cor da peca recebida como parametro."
                        return False
                else:
                    print "Existe peça no local de destino."
                    return False
            else:
                print "Nao existe nenhuma peca no local passado como origem."
                return False
        else:
            print "Coordenada passada esta fora do tabuleiro."
            return False

    """
        Verificar antes se dama pode comer!
    """
    def valida_movimento_dama(self, tabuleiro, peca, origem, destino):
        d_coluna = peca.coordenadas[0]
        d_linha = peca.coordenadas[1]
        print "dama:", d_coluna, d_linha
        i = 1
        # verificar nordeste se tem uma casa livre entre origem e destino nessa direcao antes de encontrar uma peca branca
        # se a coluna destino e maior que a origem e linha destino meno     r que linha origem movimento nordeste
        if (origem[0] < destino[0]) and (origem[1] > destino[1]):
            peca_em_coordenada = self.existe_peca_em(tabuleiro, [d_coluna + i, d_linha - i])
            if peca_em_coordenada is None: # se tem pelo menos uma casa livre a nordeste, conte quantas livres casas a nordeste tem
                while peca_em_coordenada is None:
                    print "coordenada", [d_coluna + i, d_linha - i]
                    i += 1
                    peca_em_coordenada = self.existe_peca_em(tabuleiro, [d_coluna + i, d_linha - i])

                print "1",i, (destino[0] - origem[0] > 0), (destino[0] - origem[0] <= i) , (origem[1] - destino[1] > 0) , (origem[1] - destino[1] <= i)
                print "Dama pode andar ", i, " colunas e ", i, " linhas."
                if (destino[0] - origem[0] > 0) and (destino[0] - origem[0] <= i) and (origem[1] - destino[1] > 0) and (origem[1] - destino[1] <= i):
                    print "Movimento validado da dama: ", peca.coordenadas, " para ", destino, "andando ", i, " casas a nordeste."
                    return True
                else:
                    print "Dama deve andar no minimo 1 casa a nordeste e no maximo ", i, " casas a nordeste."
                    return False
            else:
                print "Dama nao tem para onde andar, ", i - 1, " casas vazias a nordeste."
                return False
        # se a coluna destino e maior que a origem e linha destino menor que linha origem movimento noroeste
        if (origem[0] > destino[0]) and (origem[1] > destino [1]):
            peca_em_coordenada = self.existe_peca_em(tabuleiro, [d_coluna - i, d_linha - i])
            if peca_em_coordenada is None: # se tem pelo menos uma casa livre a noroeste, conte quantas casas livres a noroeste tem
                while peca_em_coordenada is None:
                    i += 1
                    peca_em_coordenada = self.existe_peca_em(tabuleiro, [d_coluna - i, d_linha - i])
                    #if peca_em_coordenada is None or not self.dentro_do_tabuleiro(peca_em_coordenada.coordenadas[0], peca_em_coordenada.coordenadas[1]): break # IF NOT PECA DENTRO DO TABULEIRO BREAK
                print "2"
                print "Dama pode andar ", i, " colunas e ", i, " linhas."
                if (origem[0] - destino[0] > 0) and (origem[0] - destino[0] <= i) and (origem[1] - destino[1] > 0) and (origem[1] - destino[1] <= i):
                    print "Movimento validado da dama: ", peca.coordenadas, " para ", destino, "andando ", i, " casas a noroeste."
                    return True
                else:
                    print "Dama deve andar no minimo 1 casa a noroeste e no maximo ", i, " casas a noroeste."
                    return False
            else:
                print "Dama nao tem para onde andar, ", i - 1, " casas vazias a noroeste."
                return False
        # se a coluna destino e maior que a origem e linha destino maior que linha origem movimento sudeste
        if (destino[0] > origem[0]) and (origem[1] > destino [1]):
            peca_em_coordenada = self.existe_peca_em(tabuleiro, [d_coluna + i, d_linha + i])
            if peca_em_coordenada is None: # se tem pelo menos uma casa livre a sudeste, conte quantas casas livres a sudeste tem
                while peca_em_coordenada is None:
                    i += 1
                    peca_em_coordenada = self.existe_peca_em(tabuleiro, [d_coluna + i, d_linha + i])

                    #if peca_em_coordenada is None or not self.dentro_do_tabuleiro(peca_em_coordenada.coordenadas[0], peca_em_coordenada.coordenadas[1]):
                    #    break # IF NOT PECA DENTRO DO TABULEIRO BREAK
                print "3"
                print "Dama pode andar ", i, " colunas e ", i, " linhas."
                if (destino[0] - origem[0] > 0) and (destino[0] - origem[0] <= i) and (destino[1] - origem[1] > 0) and (destino[1] - origem[1] <= i):
                    print "Movimento validado da dama: ", peca.coordenadas, " para ", destino, "andando ", i, " casas a sudeste."
                    return True
                else:
                    print "Dama deve andar no minimo 1 casa a sudeste e no maximo ", i, " casas a sudeste."
                    return False
            else:
                print "Dama nao tem para onde andar, ", i - 1, " casas vazias a sudeste."
                return False
        # se a coluna destino e menor que a origem e a linha destino maior que linha origem movimento sudoeste
        if (destino[0] < origem[0]) and (origem[1] < origem[0]):
            peca_em_coordenada = self.existe_peca_em(tabuleiro, [d_coluna - i, d_linha + i])
            if peca_em_coordenada is None: # se tem pelo menos uma casa livre a sudoeste, conta quantas casas livres a sudoeste tem
                while peca_em_coordenada is None:
                    i += 1
                    peca_em_coordenada = self.existe_peca_em(tabuleiro, [d_coluna - i, d_linha + i])
                    #if peca_em_coordenada is None or not self.dentro_do_tabuleiro(peca_em_coordenada.coordenadas[0], peca_em_coordenada.coordenadas[1]): break # IF NOT PECA DENTRO DO TABULEIRO BREAK
                print "4"
                print "Dama pode andar ", i, " colunas e ", i, " linhas."
                if (origem[0] - destino[0] > 0) and (origem[0] - destino[0] <= i) and (destino[1] - origem[1] > 0) and (destino[1] - origem[1] <= i):
                    print "Movimento validado da dama: ", peca.coordenadas, " para ", destino, "andando ", i, " casas a sudoeste."
                    return True
                else:
                    print "Dama deve andar no minimo 1 casa a sudoeste e no maximo ", i, " casas a sudoeste"
                    return False
            else:
                print "Dama nao tem para onde andar, ", i-1, " casas vazias a sudoeste."
                return False

    """
        Garante movimentação da peça apenas de uma casa.
        Peças do tipo dama
    """
    def valida_movimento_peca_branca(self, tabuleiro, peca, origem, destino):
        if peca.tipo == 0: #peca e pedra
            #verifica se e pra cima direita
            if (origem[0] + 1 == destino[0]) and (origem[1] - 1 == destino[1]) :
                return True
            # verifica se e pra cima esquerda
            if (origem[0] - 1 == destino[0]) and (origem[1] - 1 == destino[1]):
                return True
            else:
                print "Peca Branca", peca.coordenadas," e pedra entao pode se mover apenas uma casa para nordeste (cima direita) ou noroeste (cima esquerda)."
                return False
        if peca.tipo == 1: #peca e dama
            if self.valida_movimento_dama( tabuleiro, peca, origem, destino):
                print "Pode mover dama branca: ", peca.coordenadas #chama move dama de origem pra destino
                return True
            return False

    def valida_movimento_peca_preta(self, tabuleiro, peca, origem, destino):
        if peca.tipo == 0: #peca e pedra
            #verifica se e pra baixo direita
            if (origem[0] + 1 == destino[0]) and (origem[1] + 1 == destino[1]):
                return True
            #verifica se e pra baixo esquerda
            if (origem[0] - 1 == destino[0]) and (origem[1] + 1 == destino[1]):
                return True
            else:
                print "Peca Preta", peca.coordenadas, " e pedra entao pode se mover apenas uma casa para sudeste (baixo direita) ou sudoeste (baixo esquerda)."
                return False
        if peca.tipo == 1: #peca e dama
            if self.valida_movimento_dama(self, tabuleiro, peca, origem, destino):
                print "Pode mover dama preta: ", peca.coordenadas #chama move dama de origem pra destino
                #chama move dama de origem pra destino
                return True
            return False

    def valida_movimento_comer(self, tabuleiro, peca, origem, destino):
        if peca.tipo == 0: #peca e pedra
            #verifica se e pra baixo direita
            if (origem[0] + 2 == destino[0]) and (origem[1] + 2 == destino[1]):
                peca_caminho = self.existe_peca_em(tabuleiro, (origem[0] + 1, origem[1] + 1))
                if not peca_caminho is None and peca_caminho.cor != peca.cor:
                    print("Movimento válido, para comer")
                    return True
                print("Você não pode fazer esse movimento, apenas mover mais de 1 casa se for para comer")
                return False
            #verifica se e pra baixo esquerda
            if (origem[0] - 2 == destino[0]) and (origem[1] + 2 == destino[1]):
                peca_caminho = self.existe_peca_em(tabuleiro, (origem[0] - 1, origem[1] + 1))
                if not peca_caminho is None and peca_caminho.cor != peca.cor:
                    print("Movimento válido, para comer")
                    return True
                print("Você não pode fazer esse movimento, apenas mover mais de 1 casa se for para comer")
                return False
            #Verifica cima direita
            if (origem[0] + 2 == destino[0]) and (origem[1] - 2 == destino[1]):
                peca_caminho = self.existe_peca_em(tabuleiro, (origem[0] + 1, origem[1] - 1))
                if not peca_caminho is None and peca_caminho.cor != peca.cor:
                    print("Movimento válido, para comer")
                    return True
                print("Você não pode fazer esse movimento, apenas mover mais de 1 casa se for para comer")
                return False
            # verifica se e pra cima esquerda
            if (origem[0] - 2 == destino[0]) and (origem[1] - 2 == destino[1]):
                peca_caminho = self.existe_peca_em(tabuleiro, (origem[0] - 1, origem[1] - 1))
                if not peca_caminho is None and peca_caminho.cor != peca.cor:
                    print("Movimento válido, para comer")
                    return True
                print("Você não pode fazer esse movimento, apenas mover mais de 1 casa se for para comer")
                return False
            else:
                print "Peca", peca.coordenadas, " apenas pode se mover 2 casas para comer."
                return False
        if peca.tipo == 1: #peca e dama
            #Ainda não verifiquei para movimentação de dama
            #if self.valida_movimento_dama(self, tabuleiro, peca, origem, destino):
                #print "Pode mover dama", peca.coordenadas #chama move dama de origem pra destino
                #chama move dama de origem pra destino
            return False

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
                # print "existe peca em 1 lado: ",self.existe_peca_em(tabuleiro, [p_coluna + 1, p_linha - 1])
                # print "existe peca em 2 lado: ",self.existe_peca_em(tabuleiro, [p_coluna + 2, p_linha - 2])
                if (self.dentro_do_tabuleiro(p_coluna + 1, p_linha + 1)) and (self.dentro_do_tabuleiro(p_coluna + 2, p_linha + 2)):  # baixo direita
                    peca_em_coordenada = self.existe_peca_em(tabuleiro, [p_coluna + 1, p_linha + 1])
                    if (peca_em_coordenada is not None) and (peca_em_coordenada.cor != peca_branca.cor):
                        if self.existe_peca_em(tabuleiro, [p_coluna + 2, p_linha + 2]) is None:
                            print "Pode comer em ", p_coluna + 2, ", ",p_linha + 2
                            peca_branca.jogadas_possiveis.append([p_coluna + 2, p_linha + 2])
                            podem_comer.append(peca_branca)
                if (self.dentro_do_tabuleiro(p_coluna - 1, p_linha + 1)) and (self.dentro_do_tabuleiro(p_coluna - 2, p_linha + 2)):  # baixo esquerda
                    peca_em_coordenada = self.existe_peca_em(tabuleiro, [p_coluna - 1, p_linha + 1])
                    if (peca_em_coordenada is not None) and (peca_em_coordenada.cor != peca_branca.cor):
                        if self.existe_peca_em(tabuleiro, [p_coluna - 2, p_linha + 2]) is None:
                            peca_branca.jogadas_possiveis.append([p_coluna - 2, p_linha + 2])
                            podem_comer.append(peca_branca)
                            print "Pode comer em ", p_coluna - 2, ", ",p_linha + 2
                if (self.dentro_do_tabuleiro(p_coluna - 1, p_linha - 1)) and (self.dentro_do_tabuleiro(p_coluna - 2, p_linha - 2)):  # cima esquerda
                    peca_em_coordenada = self.existe_peca_em(tabuleiro, [p_coluna - 1, p_linha - 1])
                    if (peca_em_coordenada is not None) and (peca_em_coordenada.cor != peca_branca.cor):
                        if self.existe_peca_em(tabuleiro, [p_coluna - 2, p_linha - 2]) is None:
                            print "Pode comer em ", p_coluna - 2, "," ,p_linha - 2
                            peca_branca.jogadas_possiveis.append([p_coluna - 2, p_linha - 2])
                            podem_comer.append(peca_branca)
                if (self.dentro_do_tabuleiro(p_coluna + 1, p_linha - 1)) and (self.dentro_do_tabuleiro(p_coluna + 2, p_linha - 2)):  # cima direita
                    peca_em_coordenada = self.existe_peca_em(tabuleiro, [p_coluna + 1, p_linha - 1])
                    if (peca_em_coordenada is not None) and (peca_em_coordenada.cor != peca_branca.cor):
                        #print"peca_em_coordenada ",peca_em_coordenada.coordenadas," eh ", peca_em_coordenada.cor," = peca_branca em ",peca_branca.coordenadas," eh ", peca_branca.cor
                        if self.existe_peca_em(tabuleiro, [p_coluna + 2, p_linha - 2]) is None:
                            print "Pode comer em ",p_coluna+2, ", ",p_linha-2
                            peca_branca.jogadas_possiveis.append([p_coluna + 2, p_linha - 2])
                            podem_comer.append(peca_branca)
        if len(podem_comer) > 0:
            print "pedras brancas podem comer"
        return podem_comer

    """
        Retorna uma lista das coordenadas das damas que podem comer e informa sua lista de posições obrigatorias
        Para todos os sentidos de movimento, verifica enquando não sair do tabuleiro. Adicionar jogada obrigatoria
        Se exister peça de cor oposta com o passo seguinte vazio. Se exister alguma peça da mesma cor, sair da verificação.
    """
    def damas_podem_comer(self, tabuleiro, peca): # passar a peca serve apenas para representar de quem e a vez atual
        coordenada_dama = []
        d_coluna = peca.coordenadas[0]
        d_linha = peca.coordenadas[1]

        #PROBLEMA Do algoritmo anterior
        #Apenas verifica o proximo salto, no caso tem que estar dentro do tabuleiro e possuir uma
        # peça e a mesma tem que ser da cor oposta a peça informada, ese ccaso não ingloba todas as situações

        i=1
        #Verificar cima direita.
        possivel = True
        existe = False
        while self.dentro_do_tabuleiro(d_coluna + i, d_linha - i) and possivel:
            if self.existe_peca_em(tabuleiro, (d_coluna + i , d_linha - i)) is not None:
                if self.existe_peca_em(tabuleiro, (d_coluna + i, d_linha - i)).cor != peca.cor:
                    if (self.dentro_do_tabuleiro(d_coluna + (i + 1), d_linha - (i + 1))) and self.existe_peca_em(
                            tabuleiro, (d_coluna + (i + 1), d_linha - (i + 1))) is None:
                        peca.jogadas_possiveis.append((d_coluna + (i + 1), d_linha - (i + 1)))
                        coordenada_dama.append(peca)
                        existe = True
                else:
                    possivel = False
            else: #Ocaso vai ocorrer, se não existir nada na posição e já tiver sido add uma peça
                if existe:
                    peca.jogadas_possiveis.append((d_coluna + (i + 1), d_linha - (i + 1)))
            i += 1

        i = 1
        #Sentido Cima esquerda
        possivel = True
        existe = False
        while self.dentro_do_tabuleiro(d_coluna - i, d_linha - i) and possivel:
            if self.existe_peca_em(tabuleiro, (d_coluna - i, d_linha - i)) is not None:
                if self.existe_peca_em(tabuleiro, (d_coluna - i, d_linha - i)).cor != peca.cor:
                    if (self.dentro_do_tabuleiro(d_coluna - (i + 1), d_linha - (i + 1))) and self.existe_peca_em(
                            tabuleiro, (d_coluna - (i + 1), d_linha - (i + 1))) is None:
                        peca.jogadas_possiveis.append((d_coluna - (i + 1), d_linha - (i + 1)))
                        coordenada_dama.append(peca)
                        existe = True
                else:
                    possivel = False
            else: #Ocaso vai ocorrer, se não existir nada na posição e já tiver sido add uma peça
                if existe:
                    peca.jogadas_possiveis.append((d_coluna - (i + 1), d_linha - (i + 1)))
            i += 1

        i = 1
        #Sentido Baixo Direita
        possivel = True
        existe = False
        while self.dentro_do_tabuleiro(d_coluna + i, d_linha + i) and possivel:
            if self.existe_peca_em(tabuleiro, (d_coluna + i, d_linha + i)) is not None:
                if self.existe_peca_em(tabuleiro, (d_coluna + i, d_linha+ i)).cor != peca.cor:
                    if (self.dentro_do_tabuleiro(d_coluna + (i + 1), d_linha + (i + 1))) and self.existe_peca_em(
                            tabuleiro, (d_coluna + (i + 1), d_linha + (i + 1))) is None:
                        print "Situacao, baixo direita", (d_coluna + (i + 1), d_linha + (i + 1))
                        peca.jogadas_possiveis.append((d_coluna + (i + 1), d_linha + (i + 1)))
                        coordenada_dama.append(peca)
                        existe = True
                else:
                    possivel = False
            else: #Ocaso vai ocorrer, se não existir nada na posição e já tiver sido add uma peça
                if existe:
                    peca.jogadas_possiveis.append((d_coluna + (i + 1), d_linha + (i + 1)))

            i += 1

        i = 1
        #Sentido Baixo esquerda
        possivel = True
        existe = False
        while self.dentro_do_tabuleiro(d_coluna - i, d_linha + i) and possivel:
            if self.existe_peca_em(tabuleiro, (d_coluna - i, d_linha + i)) is not None:
                if self.existe_peca_em(tabuleiro, (d_coluna - i, d_linha + i)).cor != peca.cor:
                    if (self.dentro_do_tabuleiro(d_coluna - (i + 1), d_linha + (i + 1))) and self.existe_peca_em(
                            tabuleiro, (d_coluna - (i + 1), d_linha + (i + 1))) is None:
                        peca.jogadas_possiveis.append((d_coluna - (i + 1), d_linha + (i + 1)))
                        coordenada_dama.append(peca)
                        existe = True
                else:
                    possivel = False
            else: #Ocaso vai ocorrer, se não existir nada na posição e já tiver sido add uma peça
                if existe:
                    peca.jogadas_possiveis.append((d_coluna - (i + 1), d_linha + (i + 1)))
            i += 1
        return coordenada_dama

    """
        Verifica a quantidade de peças pretas e brancas.
        Apenas pode exister 1 peça preta no caminho da dama
        E não pode existir peças brancas nesse caminho.
    """
    def valida_caminho_dama(self, tabuleiro,peca, origem, destino):
        y = 0
        sent_y = 1 #sentido descendo
        if origem[1] > destino[1]:  # subindo
            sent_y = -1
        sent_x = 1
        if origem[0] > destino[0]:
            sent_x = -1
        mover = False
        qtdPreta = 0
        qtdBranca = 0
        for l in range(origem[0] + sent_x, destino[0] + sent_x, sent_x):
            y += sent_y
            coord = (l, origem[1] + y) #Caminha nas linhas
            for cod in tabuleiro.unifica_lista():
                if cod.coordenadas == coord:
                    print "Existe peça:", cod.cor, "no caminho"
                    if cod.cor: #Cor da peca Preta
                        qtdPreta += 1
                    else:
                        qtdBranca += 1
        if peca.cor:# Se for jogada da peca preta
            if not qtdPreta: #Quantidade de Pretas igual a zero
                if qtdBranca <= 1: #Existe no maximo 1 peça preta no caminho
                    mover = True
                else:
                    print "Você não pode comer duas peças de uma vez."
            else:
                print "Não pode existir peças pretas no caminho."
        else:
            if not qtdBranca: #Quantidade de Brancas igual a zero
                if qtdPreta <= 1: #Existe no maximo 1 peça preta no caminho
                    mover = True
                else:
                    print "Você não pode comer duas peças de uma vez."
            else:
                print "Não pode existir peças brancas no caminho."

        return mover

    def comerPreta(self, tabuleiro, peca, origem, destino):
        y = 0
        sent_y = 1 #sentido descendo
        if origem[1] > destino[1]:  # subindo
            sent_y = -1
        sent_x = 1
        if origem[0] > destino[0]:
            sent_x = -1
        comer = False
        for l in range(origem[0] + sent_x, destino[0] + sent_x, sent_x):
            y += sent_y
            coord = (l, origem[1] + y) #Caminha nas linhas
            for cod in tabuleiro.lista_das_pretas:
                if cod.coordenadas == coord:
                    tabuleiro.removePreta(cod)
                    comer = True
        return comer

    def capsula(self, tabuleiro, peca, origem, destino):
        val = comerPreta(self, tabuleiro, peca, origem, destino)
        return tabuleiro, val

    def comerBranca(self, tabuleiro, peca, origem, destino):
        y = 0
        sent_y = 1  # sentido descendo
        if origem[1] > destino[1]:  # subindo
            sent_y = -1
        sent_x = 1
        if origem[0] > destino[0]:
            sent_x = -1
        comer = False
        for l in range(origem[0] + sent_x, destino[0] + sent_x, sent_x):
            y += sent_y
            coord = (l, origem[1] + y)  # Caminha nas linhas
            for cod in tabuleiro.lista_das_brancas:
                if cod.coordenadas == coord:
                    tabuleiro.removeBranca(cod)
                    comer = True
        return comer


    def novoJogo(self):
        largura = 8
        altura = 8

        tabuleiro = Tabuleiro(largura, altura)
        jogador1 = Jogador(tabuleiro.lista_das_brancas)
        jogador2 = Jogador(tabuleiro.lista_das_pretas)

        return Jogo(jogador1, jogador2, tabuleiro)

    def salvarJogo(self, tabuleiro, nomeSave):
        caminho = "../save/" + nomeSave + '.json'
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
        caminho = "../save/" + nomeSave + '.json'

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
