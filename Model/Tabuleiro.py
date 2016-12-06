# coding: utf-8
# Tabuleiro do jogo. Precisa de uma altura e uma largura para ser instanciado
from Model.Peca import *
class Tabuleiro(object):
    PRETA = 1
    BRANCA = 0
    ND = -1

    def __init__(self, altura, largura):
        """
            Monta o tauleiro, profundidade eh estaticamente atribuida
        """
        # Define altura e largura do tabuleiro
        self.largura = largura
        self.altura = altura

        # Cria duas listas, cada uma contendo as pecas que cada jogador tem
        self.lista_das_pretas = []
        self.lista_das_brancas = []

        for l in range(0,3):
            for c in range(0,8):
                if(l % 2):
                    if(c % 2):
                        self.lista_das_pretas.append(Peca(1, (c, l), 0))
                    else:
                        self.lista_das_brancas.append(Peca(0, (c, 7 - l), 0))
                else:
                    if (c % 2):
                        self.lista_das_brancas.append(Peca(1, (c, 7 - l), 0))
                    else:
                        self.lista_das_pretas.append(Peca(0, (c, l), 0))

        # estado_tabuleiro guarda o estado atual do tabuleiro para printar e para avaliar
        self.estado_tabuleiro = [[' '] * self.largura for x in range(self.altura)]

    def printa_tabuleiro(self):
        """
            Printa o tabuleiro no console
        """
        print (Tabuleiro.__unicode__(self))

    def __unicode__(self):
        """
            Guarda o unicode e outro estado do tabuleiro para printar o tabuleiro
        """
        # Atauliza o estado do tabuleiro
        self.atualiza_tabuleiro()
        linhas = []
        # Printa o numero no topo do tabuleiro
        linhas.append('    ' + '   '.join(map(str, range(self.largura))))

        # Printa a borda de cima do tabuleiro em unicode
        linhas.append(u'  ╭' + (u'───┬' * (self.largura - 1)) + u'───╮')

        # Printa as linhas do tabuleiro
        for num, linha in enumerate(self.estado_tabuleiro[:-1]):
            linhas.append(chr(num + 65) + u' │ ' + u' │ '.join(linha) + u' │')
            linhas.append(u'  ├' + (u'───┼' * (self.largura - 1)) + u'───┤')

        # Printa a ultima linha
        linhas.append(chr(self.altura + 64) + u' │ ' + u' │ '.join(self.estado_tabuleiro[-1]) + u' │')

        # Printa a ultima linha do tabuleiro
        linhas.append(u'  ╰' + (u'───┴' * (self.largura - 1)) + u'───╯')
        return '\n'.join(linhas)

    def atualiza_tabuleiro(self):
        """
            Atualiza o array que tem o tabuleiro para representar o estado das pecas no tabuleiro
        """
        for i in range(self.largura):
            for j in range(self.altura):
                self.estado_tabuleiro[i][j] = " "

        for peca in self.lista_das_pretas:
            self.estado_tabuleiro[peca.coordenadas[1]][peca.coordenadas[0]] = u'◆'
        for peca in self.lista_das_brancas:
            self.estado_tabuleiro[peca.coordenadas[1]][peca.coordenadas[0]] = u'◇'

    def removePreta(self, peca):
        self.lista_das_pretas.remove(peca)

    def removeBranca(self, peca):
        self.lista_das_brancas.remove(peca)

    def addPeca(self, cor, coord, tipo):
        if(cor):
            self.lista_das_pretas.append(Peca(cor, (coord[0], coord[1]), tipo))
        else:
            self.lista_das_brancas.append(Peca(cor, (coord[0], coord[1]), tipo))

    def esvaziar_lista(self):
        self.lista_das_brancas = []
        self.lista_das_pretas = []