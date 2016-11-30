# coding: utf-8
# Tabuleiro do jogo. Precisa de uma altura e uma largura para ser instanciado
from Peca import *
class Tabuleiro(object):
    PRETA = 1
    BRANCA = 0
    ND = -1

    def __init__(self, altura, largura, primeiroJogador):
        """
            Monta o tauleiro, profundidade eh estaticamente atribuida
        """
        # Define altura e largura do tabuleiro
        self.largura = largura
        self.altura = altura

        # Cria duas listas, cada uma contendo as pecas que cada jogador tem
        self.lista_das_pretas = []
        self.lista_das_brancas = []

        # Colocando as pecas nas posicoes iniciais
        for i in range(largura):
            self.lista_das_pretas.append(Peca(1,(i, i % 2),0))
            self.lista_das_brancas.append(Peca(0,(i, altura - (i % 2) - 1),0))
            if (largura == 8) and (i == 0):
                self.lista_das_brancas.append(Peca(0,(i, 5),0))
                self.lista_das_brancas.append(Peca(0,(2, 5),0))
                self.lista_das_brancas.append(Peca(0,(4, 5),0))
                self.lista_das_brancas.append(Peca(0,(6, 5),0))
                self.lista_das_pretas.append(Peca(1,(i, 2),0))
                self.lista_das_pretas.append(Peca(1,(2, 2),0))
                self.lista_das_pretas.append(Peca(1,(4, 2),0))
                self.lista_das_pretas.append(Peca(1,(6, 2),0))

        # estado_tabuleiro guarda o estado atual do tabuleiro para printar e para avaliar
        self.estado_tabuleiro = [[' '] * self.largura for x in range(self.altura)]
    def printa_tabuleiro(self):
        """
            Printa o tabuleiro no console
        """
        print unicode(self)

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
