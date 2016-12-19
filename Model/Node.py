from copy import deepcopy

from Regras import *

class Node(object):

    def __init__(self, tabuleiro, vez, regras):
        self.tabuleiro = tabuleiro
        self.regras = regras
        self.vez = vez
        self.filhos = [] # Popular lista dos tabuleiros de acordo com as jogadas possiveis
        self.faz_filho()
        self.valor = 0 # Calcular a avaliacao do tabuleiro


    def faz_filho(self): # Falta implementar quando podem ser feitas mais de uma comida em uma mesma jogada
        if self.vez == 0: #vez e branco
            branca_come_preta = self.regras.pedras_podem_comer(self.tabuleiro, 0)
            if len(branca_come_preta) > 0:
                print "Branco e obrigado a comer. ", len(branca_come_preta)
                # So tabuleiro originados das comidas vao pra filhos
                numero_de_filhos = 0 # so pra debugar, isso tem que ser igual ao numero de filhos
                for peca in branca_come_preta:
                    origem = peca.coordenadas

                    for jogada in peca.jogadas_possiveis:
                        destino = jogada
                        tabuleiro_temporario = deepcopy(self.tabuleiro)
                        self.regras.mover(tabuleiro_temporario, peca.cor, [[chr(origem[1]+97), str(origem[0])], [chr(destino[1]+97), str(destino[0])]], peca.tipo)
                        numero_de_filhos += 1
                        self.filhos.append(tabuleiro_temporario)
            else: # Se nao der para comer verifica todas as pecas do jogador quais tem a diagonal livre
                numero_de_filhos = 0 # so pra debugar, isso tem que ser igual ao numero de filhos
                for peca in self.tabuleiro.lista_das_brancas:
                    if peca.tipo == 0:
                        origem = peca.coordenadas
                        destino = [peca.coordenadas[0] - 1, peca.coordenadas[1] - 1] # Testa noroeste

                        if self.pode_ir(self.tabuleiro, destino):
                            tabuleiro_temporario = deepcopy(self.tabuleiro)
                            self.regras.mover(tabuleiro_temporario, peca.cor, [[chr(origem[1]+97), str(origem[0])], [chr(destino[1]+97), str(destino[0])]], peca.tipo)
                            numero_de_filhos += 1
                            self.filhos.append(tabuleiro_temporario)


                        #print "passando pra testar nordeste"

                        #self.tabuleiro.printa_tabuleiro()

                        destino = [peca.coordenadas[0] + 1, peca.coordenadas[1] - 1] # Testa nordeste
                        if self.pode_ir(self.tabuleiro, destino):
                            tabuleiro_temporario = deepcopy(self.tabuleiro)
                            self.regras.mover(tabuleiro_temporario, peca.cor, [[chr(origem[1]+97), str(origem[0])], [chr(destino[1]+97), str(destino[0])]], peca.tipo)
                            numero_de_filhos += 1
                            self.filhos.append(tabuleiro_temporario)
                    #FALTA VER OS MOVIMENTOS DA DAMA

        else:
            # Vez e do preto
            preta_come_branca = self.regras.pedras_podem_comer(self.tabuleiro, 1)
            if len(preta_come_branca) > 0:
                print "Preto e obrigado a comer. "
                # So tabuleiro originados das comidas vao pra filhos
                numero_de_filhos = 0 # So pra debugar
                for peca in preta_come_branca:
                    origem = peca.coordenadas
                    for jogada in peca.jogadas_possiveis:
                        destino = jogada
                        tabuleiro_temporario = deepcopy(self.tabuleiro)
                        self.regras.mover(tabuleiro_temporario, peca.cor, [[chr(origem[1]+97), str(origem[0])], [chr(destino[1]+97), str(destino[0])]], peca.tipo)
                        numero_de_filhos += 1
                        self.filhos.append(tabuleiro_temporario)
            else: # Se nao der pra comer verifica todas as pecas do jogados quais tem a diagonal livre
                numero_de_filhos = 0
                for peca in self.tabuleiro.lista_das_pretas:
                    if peca.tipo == 0:
                        origem = peca.coordenadas
                        destino = [peca.coordenadas[0] - 1, peca.coordenadas[1] + 1]  # Testa sudeste
                        if self.pode_ir(self.tabuleiro, destino):

                            tabuleiro_temporario = deepcopy(self.tabuleiro)
                            self.regras.mover(tabuleiro_temporario, peca.cor, [[chr(origem[1]+97), str(origem[0])], [chr(destino[1]+97), str(destino[0])]], peca.tipo)
                            numero_de_filhos += 1
                            self.filhos.append(tabuleiro_temporario)

                        destino = [peca.coordenadas[0] + 1, peca.coordenadas[1] + 1]  # Testa sudoeste
                        if self.pode_ir(self.tabuleiro, destino):
                            tabuleiro_temporario = deepcopy(self.tabuleiro)
                            self.regras.mover(tabuleiro_temporario, peca.cor, [[chr(origem[1]+97), str(origem[0])], [chr(destino[1]+97), str(destino[0])]], peca.tipo)
                            numero_de_filhos += 1
                            self.filhos.append(tabuleiro_temporario)

                    # FALTA VER OS MOVIMENTOS DA DAMA
        print "*********************** QUANTIDADE DE FILHOS *********************** ", len(self.filhos)
        for filho in self.filhos:
            filho.printa_tabuleiro()

    def pode_ir(self, tabuleiro, destino):
        if self.regras.dentro_do_tabuleiro(destino[0], destino[1]):
            if self.regras.existe_peca_em(tabuleiro, [destino[0], destino[1]]) is None:
                return True
        return False


