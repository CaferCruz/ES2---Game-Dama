class Peca(object):

    def __init__(self, cor, coordenadas, tipo):
        self.cor = cor # 0 eh branca e 1 eh preta
        self.coordenadas = coordenadas
        self.tipo = tipo # 0 eh pedra e 1 eh dama
        self.jogadas_possiveis = []

    def printa_peca(self):
        print "cor: ",self.cor," , \ncoordenadas: ", self.coordenadas," , \ntipo: ", self.tipo," ,\njogadas possiveis", self.jogadas_possiveis