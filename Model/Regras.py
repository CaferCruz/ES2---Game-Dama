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

    def valida_mover(self,tabuleiro,peca,origem,destino):
        """
        # for na lista das pecas do tabuleiro do inimigo e
        # verfica se alguma peca esta na casa diagonal esq e dir
        # for na lista das pecas do tabuleiro das proprias pecas e
        # verfica se alguma peca esta na casa diagonal esq e dir
        # se estiver livre coloque essa posicao na lista de jogadas possiveis
        """
        pode_comer = []
        tem_peca_atras = False
        if peca.cor == 0: #peca branca
            for peca_branca in tabuleiro.lista_das_brancas:
                    if peca_branca.tipo == 0: #se peca é pedra
                        # verficar se e posssivel comer
                        for peca_preta in tabuleiro.lista_das_pretas: # for na lista das pecas do adversario
                            pode_comer=[]
                            if peca_preta.coordenadas[0] == peca_branca.coordenadas[0]+1 and tabuleiro.lista_das_pretas.coordenada[1] == peca_branca.coordenadas[1]-1:
                                # se existe alguma peca nas casas diagonais a frente
                                # verifique se a casa na diagonal da peca do inimigo esta livre (a direita)
                                for peca_preta_detras in tabuleiro.lista_das_pretas:
                                    if peca_preta_detras.coordenadas[0] == peca_branca.coordenadas[0]+2 and peca_preta_detras.coordenadas[1] == peca_branca.coordenadas[1]-2:
                                       tem_peca_atras = True #se tem peca atras
                                if not tem_peca_atras: #se nao tem peca preta atras verifica se tem peca branca atras
                                    for peca_branca_detras in tabuleiro.lista_das_brancas:
                                        if not peca_branca_detras.coordenadas[0] == peca_branca.coordenadas[
                                            0] + 2 and peca_branca_detras.coordenadas[1] == peca_branca.coordenadas[
                                            1] - 2:
                                            peca_branca.jogadas_possiveis.append(
                                                [peca_branca.coordenadas[0] + 2, peca_branca.coordenadas[1] - 2])
                                            pode_comer.append(peca_branca.coordenadas)
                            tem_peca_atras = False

                            if peca_preta.coordenadas[0] == peca_branca.coordenadas[0]-1 and \
                               peca_preta.coordenadas[1] == peca_branca.coordenadas[1]-1 :
                                # se existe alguma peca nas casas diagonais a frente
                                # verifique se a casa na diagonal da peca do inimigo esta livre (a esquerda)
                                for peca_preta_detras in tabuleiro.lista_das_pretas:
                                    if peca_preta_detras.coordenadas[0] == peca_branca.coordenadas[0] - 2 and \
                                                    peca_preta_detras.coordenadas[1] == peca_branca.coordenadas[1] - 2:
                                        tem_peca_atras = True  # se tem peca atras
                                if not tem_peca_atras:  # se nao tem peca preta atras verifica se tem peca branca atras
                                    for peca_branca_detras in tabuleiro.lista_das_brancas:
                                        if not peca_branca_detras.coordenadas[0] == peca_branca.coordenadas[
                                            0] - 2 and peca_branca_detras.coordenadas[1] == peca_branca.coordenadas[
                                            1] - 2:
                                            peca_branca.jogadas_possiveis.append(
                                                [peca_branca.coordenadas[0] - 2,peca_branca.coordenadas[1] - 2])
                                            pode_comer.append(peca_branca.coordenadas)
                            tem_peca_atras = False




                        

        



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