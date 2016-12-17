# coding: utf-8
# Tabuleiro do jogo. Precisa de uma altura e uma largura para ser instanciado
<<<<<<< HEAD
# MODIFIED
# Created by Carson Wilcox for Professor Szpakowicz's AI class CSI 4106

from Model.Peca import *
=======
from Peca import *
>>>>>>> 463657bcd9dfb6d71309bb4a2aa14cc825a98135
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

        """self.lista_das_brancas.append(Peca(0, (1, 5), 0))
        self.lista_das_brancas.append(Peca(0, (3, 5), 0))
        self.lista_das_brancas.append(Peca(0, (5, 5), 0))
        self.lista_das_brancas.append(Peca(0, (7, 5), 0))

        self.lista_das_brancas.append(Peca(0, (0, 6), 0))
        self.lista_das_brancas.append(Peca(0, (2, 6), 0))
        self.lista_das_brancas.append(Peca(0, (4, 6), 0))
        self.lista_das_brancas.append(Peca(0, (6, 6), 0))

        self.lista_das_brancas.append(Peca(0, (1, 7), 0))
        self.lista_das_brancas.append(Peca(0, (3, 7), 0))
        self.lista_das_brancas.append(Peca(0, (5, 7), 0))
        self.lista_das_brancas.append(Peca(0, (7, 7), 0))

        self.lista_das_pretas.append(Peca(1, (0, 2), 0))
        self.lista_das_pretas.append(Peca(1, (2, 2), 0))
        self.lista_das_pretas.append(Peca(1, (4, 2), 0))
        self.lista_das_pretas.append(Peca(1, (6, 2), 0))

        self.lista_das_pretas.append(Peca(1, (1, 1), 0))
        self.lista_das_pretas.append(Peca(1, (3, 1), 0))
        self.lista_das_pretas.append(Peca(1, (5, 1), 0))
        self.lista_das_pretas.append(Peca(1, (7, 1), 0))

        self.lista_das_pretas.append(Peca(1, (0, 0), 0))
        self.lista_das_pretas.append(Peca(1, (2, 0), 0))
        self.lista_das_pretas.append(Peca(1, (4, 0), 0))
        self.lista_das_pretas.append(Peca(1, (6, 0), 0))
        """

        for l in range(0, 3):
            for c in range(0, 8):
                if (l % 2):
                    if (c % 2):
                        self.lista_das_pretas.append(Peca(1, (c, l), 0))
                    else:
                        self.lista_das_brancas.append(Peca(0, (c, 7 - l), 0))
                else:
                    if (c % 2):
                        self.lista_das_brancas.append(Peca(0, (c, 7 - l), 0))
                    else:
                        self.lista_das_pretas.append(Peca(1, (c, l), 0))
<<<<<<< HEAD

=======
>>>>>>> 463657bcd9dfb6d71309bb4a2aa14cc825a98135
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
            print(peca.coordenadas)
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

    def unifica_lista(self):
        return self.lista_das_brancas + self.lista_das_pretas

    def get_coodenada(self, coordenada):
        lista_de_pecas = self.unifica_lista()

        for p in lista_de_pecas:
            if p.coordenadas == coordenada:
                return p
        return None