from Model.Peca import *
from Model.Jogo import *
import os
import json
from tabuleiro import tabuleiro


class Regras(object):

    # Regra de empate definida pelo grupo. 20 rodadas(1 rodada = 1 jogada preta e 1 jogada branca) sem ninguem comer ninguem
    def empate(self,rodadasSemComer):
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
    def virarDama( peca, altura):
        if peca.tipo == 1:
            return False
        if peca.coordenadas[1] == 0 and peca.cor == 0:
            return True
        if peca.coordenadas[1] == altura and peca.cor == 1:
            return True
        return False

    def mover(self,tabuleiro, cor):
        if(cor == 0): # Peca branca
            # aviso1 = "Escolha uma peca sua para mover... " + chr(t.lista_das_brancas[0][0] + 97) + str(t.lista_das_brancas[0][1])
            print("informe a jogada:")
            while True:  # Enquanto nao receber input valido

                jogada = []

                jogada = raw_input().lower().split()

                if not (len(jogada) == 2):
                    print("Essa jogada nao e valida, tente novamente.", " aviso1")
                    continue
                origem = (int(jogada[0][1]), ord(jogada[0][0]) - 97)
                peca = Peca(0, origem, 0)
                destino = (int(jogada[1][1]), ord(jogada[1][0]) - 97)

                pecab = peca
                pertence = False
                # A peca movida pertence ao jogador?
                for pecab in tabuleiro.lista_das_brancas:
                    if pecab.coordenadas == peca.coordenadas:
                        pertence = True
                        break

                if not (pertence):
                    print("peca: ", peca, " esta dentro de ", tabuleiro.lista_das_brancas)
                    print("Voce nao pertence a peca ", origem,
                          ". Por favor, selecione uma das suas pecas.")  # , t.lista_das_brancas
                    continue
                break

            self.comerPreta(tabuleiro, peca, origem, destino)
            jogada = (peca, destino)
            return jogada
        else:
            # aviso1 = "Escolha uma peca sua para mover... " + chr(t.lista_das_brancas[0][0] + 97) + str(t.lista_das_brancas[0][1])
            print("informe a jogada:")
            while True:  # Enquanto nao receber input valido
                jogada = []
                jogada = raw_input().lower().split()
                if not (len(jogada) == 2):
                    print("Essa jogada nao e valida, tente novamente.", " aviso1")
                    continue
                origem = (int(jogada[0][1]), ord(jogada[0][0]) - 97)
                peca = Peca(1, origem, 0)
                destino = (int(jogada[1][1]), ord(jogada[1][0]) - 97)

                pecab = peca
                pertence = False
                # A peca movida pertence ao jogador?
                for pecab in tabuleiro.lista_das_pretas:
                    if pecab.coordenadas == peca.coordenadas:
                        pertence = True
                        break

                if not (pertence):
                    print("peca: ", peca, " esta dentro de ", tabuleiro.lista_das_pretas)
                    print("Voce nao pertence a peca ", origem,
                          ". Por favor, selecione uma das suas pecas.")  # , t.lista_das_brancas
                    continue
                break
            self.comerBranca(tabuleiro, peca, origem, destino)
            jogada = (peca, destino)

            return jogada
        return None

    def comerPreta(self, tabuleiro, peca, origem, destino):
        y = 0
        if(origem[0] < destino[0]):
            for l in range(origem[0] + 1, destino [0] + 1):
                y = y + 1
                coord = (l, origem[1] - y)
                for cod in tabuleiro.lista_das_pretas:
                    if cod.coordenadas == coord:
                        tabuleiro.removePreta(cod)
        else:
            print(origem[0], origem[1])
            for l in range(origem[0] - 1, destino[0] -1, -1):
                print(origem[0] - 1, destino[0] -1)
                y = y - 1
                coord = (l, origem[1] + y)
                for cod in tabuleiro.lista_das_pretas:
                    if cod.coordenadas == coord:
                        tabuleiro.removePreta(cod)

    def comerBranca(self, tabuleiro, peca, origem, destino):
        y = 0
        print('origem:', origem[0],origem[1])
        if(origem[0] > destino[0]):
            for l in range(origem[0] - 1, destino [0] - 1, -1):
                y = y + 1
                coord = (l, origem[1] + y)
                print(coord)
                for cod in tabuleiro.lista_das_brancas:
                    if cod.coordenadas == coord:
                        tabuleiro.removeBranca(cod)
        else:
            for l in range(origem[0] + 1, destino[0]+1):
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

    def salvarJogo(self, NomeSave):
        caminho = "../save/" + NomeSave
        dados_json = {}
        dados = []
        dados_json["altura"] = 8
        dados_json["largura"] = 8


        with open(caminho, 'w') as outfile:
            json.dump(dados_json, outfile)
        return None
















