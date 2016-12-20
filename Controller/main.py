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
                j = regras.carregarJogo('save')
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
                regras.salvarJogo(tabuleiro, "save")
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
        total_mv = True
        while total_mv:  # Enquanto receber input invalido
            print("informe a jogada:")
            jogada = raw_input().lower().split()
            if len(jogada) == 2:
                origem = (int(jogada[0][1]), ord(jogada[0][0]) - 97)
                peca = regras.existe_peca_em(tabuleiro, origem)
                destino = (int(jogada[1][1]), ord(jogada[1][0]) - 97)
                regra_mover = regras.valida_mover(tabuleiro, peca, origem, destino)

                if regra_mover:
                    lista_mv_obg = regras.pedras_podem_comer(tabuleiro, corPeca)
                    for m in lista_mv_obg:
                        print("Obrigatorio comer com a peca: ", m.coordenadas)
                    mv_obrigatorio = regras.mover_obrigatorio(tabuleiro, origem, destino, lista_mv_obg)

                    if not lista_mv_obg or mv_obrigatorio:
                        total_mv = regras.mover(tabuleiro, corPeca, jogada)
                        tabuleiro.printa_tabuleiro()
                    else:
                        print("Você é obrigado a comer.")
                else:
                    print("Essa jogada não está entre os critérios válidos")
            else:
                print("Jogada não e válida, tente novamente:")

    ### MAIN  ###
    nome = "Lucas"
    print("######\tDamEX\t######")
    print("Comandos: Mover -> posInicio posDestino, ex: a1 b2")
    print("Comando: save")
    print("######################")

    tabuleiro = initJogo()


    # loop
    while regras.vitoria(tabuleiro) == -1:

        # Usuario comeca jogando
        print(">>>>>>>SUA VEZ.<<<<<<<<")
        mover(tabuleiro, 0)

        if regras.vitoria(tabuleiro) == 0:
            print ("Usuario ganhou o jogo")
            print ("Game Over")
            break
        print ("~~~~~~~~~~~~JOGADA DO COMPUTADOR~~~~~~~~~~~~")

        print ("Seu adversario ira jogar!")
        mover(tabuleiro, 1)

        if regras.vitoria(tabuleiro) == 1:
            print ("Computador ganhou o jogo")
            print ("Game Over")
            break
        salvarJogo(tabuleiro)

