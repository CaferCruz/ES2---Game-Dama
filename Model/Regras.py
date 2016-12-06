from Model.Peca import *
from tabuleiro import tabuleiro


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
    def virarDama(peca, altura):
        if peca.tipo == 1:
            return False
        if peca.coordenadas[1] == 0 and peca.cor == 0:
            return True
        if peca.coordenadas[1] == altura and peca.cor == 1:
            return True
        return False

    # TODO: corrigir validação, peças se movimentam em qualquer direção
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

    def valida_mover(self, tabuleiro, peca, origem, destino):  # Verificar antes se jogador eh obrigado a comer, se ela for comer nem chame essa funcao
        """
        Verificar antes se jogador eh obrigado a comer
        """
        peca_em_coordenada = existe_peca_em(tabuleiro, peca.coordenadas)
        if dentro_do_tabuleiro(origem[0], origem[1]) and dentro_do_tabuleiro(destino[0], destino[1]): #se origem e destino esta dentro do tabuleiro
            if peca_em_coordenada is not None: # se tem alguma peca
                if peca.cor == peca_em_coordenada.cor: #se a peca que esta na casa eh da cor da peca que foi passada
                    if peca.cor == 0:
                        if valida_movimento_peca_branca(tabuleiro, peca, origem, destino):
                            print "Pode mover peca ", peca.coordenadas #CHAMA A FUNCAO DE MOVER AGORA!!!!
                    elif peca.cor == 1:
                        if valida_movimento_peca_preta(tabuleiro, peca, origem, destino):
                            print "Pode mover peca ", peca.coordenadas #CHAMA A FUNCAO DE MOVER AGORA!!!!
                else:
                    print "Cor da peca encontrada em origem diferente da cor da peca recebida como parametro."
            else:
                print "Nao existe nenhuma peca no local passado como origem."
        else:
            print "Coordenada passada esta fora do tabuleiro."

    def valida_movimento_dama(self, tabuleiro, peca, origem, destino):
        coluna = peca.coordenadas[0]
        linha = peca.coordenadas[1]
        i = 1
        # verificar nordeste se tem uma casa livre entre origem e destino nessa direcao antes de encontrar uma peca branca
        # se a coluna destino e maior que a origem e linha destino menor que linha origem movimento nordeste
        if (origem[0] < destino[0]) and (origem[1] > destino[1]):
            peca_em_coordenada = existe_peca_em(tabuleiro, [coluna + i, linha - i])
            if peca_em_coordenada is None: # se tem pelo menos uma casa livre a nordeste, conte quantas livres casas a nordeste tem
                while peca_em_coordenada is None:
                    i += 1
                    peca_em_coordenada = existe_peca_em(tabuleiro, [coluna + i, linha - i])
                    #IF NOT PECA DENTRO DO TABULEIRO BREAK
                    if not dentro_do_tabuleiro(peca_em_coordenada[0], peca_em_coordenada[1]): break
                print "Dama pode andar ", i, " colunas e ", i, " linhas."
                if (destino[0] - origem[0] > 0) and (destino[0] - origem[0] <= i) and (origem[1] - destino[1] > 0) and (origem[1] - destino[1] <= i):
                    print "Movimento validado da dama: ", peca.coordenadas, " para ", destino, "andando ", i, " casas a nordeste."
                    return True
                else: print "Dama deve andar no minimo 1 casa a nordeste e no maximo ", i, " casas a nordeste."
            else:
                print "Dama nao tem para onde andar, ", i - 1, " casas vazias a nordeste."
        # se a coluna destino e maior que a origem e linha destino menor que linha origem movimento noroeste
        if (origem[0] > destino[0]) and (origem[1] > destino [1]):
            peca_em_coordenada = existe_peca_em(tabuleiro, [coluna - i, linha - i])
            if peca_em_coordenada is None: # se tem pelo menos uma casa livre a noroeste, conte quantas casas livres a noroeste tem
                while peca_em_coordenada is None:
                    i += 1
                    peca_em_coordenada = existe_peca_em(tabuleiro, [coluna - i, linha - i])
                    # IF NOT PECA DENTRO DO TABULEIRO BREAK
                    if not dentro_do_tabuleiro(peca_em_coordenada[0], peca_em_coordenada[1]): break
                print "Dama pode andar ", i, " colunas e ", i, " linhas."
                if (origem[0] - destino[0] > 0) and (origem[0] - destino[0] <= i) and (origem[1] - destino[1] > 0) and (origem[1] - destino[1] <= i):
                    print "Movimento validado da dama: ", peca.coordenadas, " para ", destino, "andando ", i, " casas a noroeste."
                    return True
                else: print "Dama deve andar no minimo 1 casa a noroeste e no maximo ", i, " casas a noroeste."
            else:
                print "Dama nao tem para onde andar, ", i - 1, " casas vazias a noroeste."
        # se a coluna destino e maior que a origem e linha destino maior que linha origem movimento sudeste
        if (destino[0] > origem[0]) and (origem[1] > destino [1]):
            peca_em_coordenada = existe_peca_em(tabuleiro, [coluna + i, linha + i])
            if peca_em_coordenada is None: # se tem pelo menos uma casa livre a sudeste, conte quantas casas livres a sudeste tem
                while peca_em_coordenada is None:
                    i += 1
                    peca_em_coordenada = existe_peca_em(tabuleiro, [coluna + i, linha + i])
                    # IF NOT PECA DENTRO DO TABULEIRO BREAK
                    if not dentro_do_tabuleiro(peca_em_coordenada[0], peca_em_coordenada[1]): break
                print "Dama pode andar ", i, " colunas e ", i, " linhas."
                if (destino[0] - origem[0] > 0) and (destino[0] - origem[0] <= i) and (destino[1] - origem[1] > 0) and (destino[1] - origem[1] <= i):
                    print "Movimento validado da dama: ", peca.coordenadas, " para ", destino, "andando ", i, " casas a sudeste."
                    return True
                else: print "Dama deve andar no minimo 1 casa a sudeste e no maximo ", i, " casas a sudeste."
            else:
                print "Dama nao tem para onde andar, ", i - 1, " casas vazias a sudeste."
        # se a coluna destino e menor que a origem e a linha destino maior que linha origem movimento sudoeste
        if (destino[0] < origem[0]) and (origem[1] < origem[0]):
            peca_em_coordenada = existe_peca_em(tabuleiro, [coluna - i, linha + i])
            if peca_em_coordenada is None: # se tem pelo menos uma casa livre a sudoeste, conta quantas casas livres a sudoeste tem
                while peca_em_coordenada is None:
                    i += 1
                    peca_em_coordenada = existe_peca_em(tabuleiro, [coluna - i, linha + i])
                    # IF NOT PECA DENTRO DO TABULEIRO BREAK
                    if not dentro_do_tabuleiro(peca_em_coordenada[0], peca_em_coordenada[1]): break
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
            if valida_movimento_dama(self, tabuleiro, peca, origem, destino):
                print "Pode mover dama branca: ", peca.coordenadas #chama move dama de origem pra destino

    def valida_movimento_peca_preta(self, peca, origem, destino):
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
            if valida_movimento_dama(self, tabuleiro, peca, origem, destino):
                print "Pode mover dama preta: ", peca.coordenadas #chama move dama de origem pra destino
                #chama move dama de origem pra destino

    def pedras_pretas_podem_comer(self, tabuleiro):
        """
        Retorna lista de pedras pretas que podem comer e
        atribui as movimentacoes as jogadas possiveis da peca
        se a lista for vazia nao existe movimento para comer
        """
        podem_comer = []
        for peca_preta in tabuleiro.lista_das_pretas:
            if peca_preta.tipo == 0:
                coluna = peca_preta.coordenadas[0]
                linha = peca_preta.coordenadas[1]
                if (dentro_do_tabuleiro(coluna + 1, linha + 1)) and (dentro_do_tabuleiro(coluna + 2, linha + 2)):  # baixo direita
                    peca_em_coordenada = existe_peca_em(tabuleiro, [coluna + 1, linha + 1])
                    if (peca_em_coordenada is not None) and (peca_em_coordenada.cor != peca_preta.cor):
                        if existe_peca_em(tabuleiro, [coluna + 2, linha + 2]) is None:
                            peca_preta.jogadas_possiveis.append([coluna + 2, linha + 2])
                            podem_comer.append(peca_preta)
                if (dentro_do_tabuleiro(coluna - 1, linha + 1)) and (dentro_do_tabuleiro(coluna - 2, linha + 2)):  # baixo esquerda
                    peca_em_coordenada = existe_peca_em(tabuleiro, [coluna - 1, linha + 1])
                    if (peca_em_coordenada is not None) and (peca_em_coordenada.cor != peca_preta.cor):
                        if existe_peca_em(tabuleiro, [coluna - 2, linha + 2]) is None:
                            peca_preta.jogadas_possiveis.append([coluna - 2, linha + 2])
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
                if (dentro_do_tabuleiro(coluna - 1, linha - 1)) and (dentro_do_tabuleiro(coluna - 2, linha - 2)):  # cima esquerda
                    peca_em_coordenada = existe_peca_em(tabuleiro, [coluna - 1, linha - 1])
                    if (peca_em_coordenada is not None) and (peca_em_coordenada.cor != peca_branca.cor):
                        if existe_peca_em(tabuleiro, [coluna - 2, linha - 2]) is None:
                            peca_branca.jogadas_possiveis.append([coluna - 2, linha - 2])
                            podem_comer.append(peca_branca)
                if (dentro_do_tabuleiro(coluna + 1, linha - 1)) and (dentro_do_tabuleiro(coluna + 2, linha - 2)):  # cima direita
                    peca_em_coordenada = existe_peca_em(tabuleiro, [coluna + 1, linha - 1])
                    if (peca_em_coordenada is not None) and (peca_em_coordenada.cor != peca_branca.cor):
                        if existe_peca_em(tabuleiro, [coluna + 2, linha - 2]) is None:
                            peca_branca.jogadas_possiveis.append([coluna + 2, linha - 2])
                            podem_comer.append(peca_branca)
        return podem_comer

    def damas_podem_comer(self, tabuleiro, peca):
        podem_comer[]


    def dentro_do_tabuleiro(self, coluna, linha):
        if (coluna < 0) or (coluna > 7) or (linha < 0) or linha(linha > 7):
            print "coordenada: (coluna: ", coluna, ", linha: ", linha, ") nao esta dentro do tabuleiro."
            return False
        return True

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
