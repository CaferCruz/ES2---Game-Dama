#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Main conduz o jogo
from Model.Minmax import *
from Model.Tabuleiro import *

from Model.Jogador import *
from Model.Regras import *
from Model.Peca import *
from Model.Jogo import *

# Configura os tamanhos do tabuleiro
regras = Regras()

# Recebe o input do usuario



class Main(object):

    def initJogo():
        while (True):
            print("Gostaria de abrir um jogo salvo? s/n")
            resp = raw_input().lower()

            if str(resp) == 's':
                j = regras.carregarJogo('save.json')
                j.tabuleiro.printa_tabuleiro()
                return j.tabuleiro
                break
            else:
                if str(resp) == 'n':
                    j = regras.novoJogo()
                    j.tabuleiro.printa_tabuleiro()
                    return j.tabuleiro
                    break

            print ("Escolha invalida, tente novamente")

    def salvarJogo(tabuleiro):
        while (True):
            print("Deseja salvar o jogo? s/n")
            resp = raw_input().lower()

            if str(resp) == 's':
                regras.salvarJogo(tabuleiro, "save.json")
                print("Jogo salvo com sucesso.")
                break
            else:
                if str(resp) == 'n':
                    break

            print ("Escolha invalida, tente novamente")

        return None

    """
        Verifica se joga está no formato correto e se a peça é do jogador.
    """
    def mover(tabuleiro, corPeca):
        print("informe a jogada:")
        while True:  # Enquanto receber input invalido
            jogada = raw_input().lower().split()
            if len(jogada) == 2:
                pecaValida = regras.pecas_validas(tabuleiro, jogada, corPeca)
                if pecaValida:
                    return regras.mover(tabuleiro, corPeca, jogada, 0)
                print("Essa peça não pertence ao jogador.")
            print("Jogada não e válida, tente novamente:")

    ### MAIN  ###
    nome = "Lucas"
    print("######\tDamEX\t######")
    print("Comandos: Mover -> posInicio posDestino, ex: a1 b2")
    print("Comando: save")
    print("######################")

    tabuleiro = initJogo()

    # Inicializando tabuleiro para testes de pode comer
    """p = Peca(1, (5, 5), 0)
    p1 = Peca(1, (3, 5), 0)
    p2 = Peca(1, (3, 3), 0)
    p3 = Peca(1, (5, 3), 0)
    p4 = Peca(1, (0, 0), 0)
    list =[p,p1,p2,p3, p4]
    tabuleiro.lista_das_pretas = list
    b = Peca(0,(4,4),0)
    b1 = Peca (0,(1,1),0)
    list = [b,b1]
    tabuleiro.lista_das_brancas = list
    tabuleiro.printa_tabuleiro()"""

    # loop
    while regras.vitoria(tabuleiro) == -1:
        # Usuario comeca jogando
        mover(tabuleiro, 0)
        #jogada_usuario = regras.mover(tabuleiro, 0)

        tabuleiro.printa_tabuleiro()

        # Segundo jogador / IA
        print ("Seu adversario ira jogar!")
        mover(tabuleiro, 1)
        #jogada_usuario = regras.mover(tabuleiro, 1)

        print ("~~~~~~~~~~~~JOGADA DO COMPUTADOR~~~~~~~~~~~~")
        tabuleiro.printa_tabuleiro()
        salvarJogo(tabuleiro)
        if regras.vitoria(tabuleiro) == 0:
            print ("Usuario ganhou o jogo")
            print ("Game Over")
            break
        elif regras.vitoria(tabuleiro) == 1:
            print ("Computador ganhou o jogo")
            print ("Game Over")
            break


