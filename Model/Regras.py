from Model.Peca import *
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


    #TODO: corrigir validação, peças se movimentam em qualquer direção
    """
    def mover(self,tabuleiro, cor):  #valida movimento
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
    """

    def existe_peca_em(self, tabuleiro, coordenada):
        """
        Retorna a peca se existente na coordenada passada
        Senao retorna None
        """
        for peca_branca in tabuleiro.lista_das_brancas:
            if peca_branca.coordenadas == coordenada:
                return peca_branca
        for peca_preta in tabuleiro.lista_das_pretas:
            if peca_preta.coordenadas == coordenada:
                return peca_preta
        return None


    def valida_mover(self,tabuleiro,peca,origem,destino):
        """
        Se voce nao eh obrigado a comer entao ve se o movimento
        esta dentro do tabuleiro e esta sendo feito com uma peca que voce pertence

        """


    def pedras_pretas_podem_comer(self, tabuleiro): #retorna lista de pecas pretas QUE PODEM COMER
        """
        Retorna lista de pedras pretas que podem comer e
        atribui as movimentacoes as jogadas possiveis da peca
        se a lista for vazia nao existe movimento para comer
        """
        podem_comer = []
        for peca_preta in tabuleiro.lista_das_pretas:
            if peca_preta.tipo == 0:
                coluna = peca_branca.coordenadas[0]
                linha = peca_branca.coordenadas[1]
                if (dentro_do_tabuleiro(coluna + 1, linha + 1)) and (dentro_do_tabuleiro(coluna + 2, linha + 2)): #baixo direita
                    peca_em_coordenada = existe_peca_em(tabuleiro, [peca_preta.coordenadas[0] + 1, peca_preta.coordenadas[1] + 1])
                    if (peca_em_coordenada is not None) and (peca_em_coordenada.cor != peca_preta.cor):
                        if existe_peca_em(tabuleiro, [peca_preta.coordenadas[0] + 2, peca_preta.coordenadas[1] + 2]) is None:
                            peca_preta.jogadas_possiveis.append([peca_preta.coordenadas[0] + 2, peca_preta.coordenadas[1] + 2])
                            podem_comer.append(peca_preta)
                if (dentro_do_tabuleiro(coluna - 1, linha + 1)) and (dentro_do_tabuleiro(coluna - 2, linha + 2)): #baixo esquerda
                    peca_em_coordenada = existe_peca_em(tabuleiro, [peca_preta.coordenadas[0] - 1, peca_preta.coordenadas[1] + 1])
                    if (peca_em_coordenada is not None) and (peca_em_coordenada.cor != peca_preta.cor):
                        if existe_peca_em(tabuleiro, [peca_preta.coordenadas[0] - 2, peca_em_coordenada[1] + 2]) is None:
                            peca_preta.jogadas_possiveis.append([peca_preta.coordenadas[0] - 2, peca_preta.coordenadas[1] + 2])
                            podem_comer.append(peca_preta)
        return podem_comer

    def pedras_brancas_podem_comer(self, tabuleiro):
        """
        Retorna lista de pedras brancas que podem comer e
        atribui as movimentacoes as jogadas possiveis da peca
        se a lista for vazia nao existe movimento para comer
        """
        podem_comer = []
        for peca_branca in tabuleiro.lista_das_brancas:
            if peca_branca.tipo == 0:
                coluna = peca_branca.coordenadas[0]
                linha = peca_branca.coordenadas[1]
                if (dentro_do_tabuleiro(coluna - 1, linha - 1)) and (dentro_do_tabuleiro(coluna - 2, linha - 2)): # cima esquerda
                    peca_em_coordenada = existe_peca_em(tabuleiro, [coluna - 1, linha - 1])
                    if (peca_em_coordenada is not None) and (peca_em_coordenada.cor != peca_branca.cor):
                        if existe_peca_em(coluna - 2, linha - 2) is None:
                            peca_branca.jogadas_possiveis.append(coluna - 2, linha - 2)
                            podem_comer.append(peca_branca)
                if (dentro_do_tabuleiro(coluna + 1, linha - 1)) and (dentro_do_tabuleiro(coluna + 2, linha - 2)): # cima direita
                    peca_em_coordenada = existe_peca_em(tabuleiro, [coluna + 1, linha - 1])
                    if (peca_em_coordenada is not None) and (peca_em_coordenada.cor != peca_branca.cor):
                        if existe_peca_em(coluna + 2, linha - 2) is None:
                            peca_branca.jogadas_possiveis.append(coluna + 2, linha - 2)
                            podem_comer.append(peca_branca)


    def dentro_do_tabuleiro(self, coluna, linha):
        if(coluna < 0) or (coluna > 7) or (linha < 0) or linha (linha > 7):
            return False
        print "coordenada: (coluna: ", coluna,", linha: ",linha, ") nao esta dentro do tabuleiro."
        return True

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