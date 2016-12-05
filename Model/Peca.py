class Peca(object):

    def __init__(self, cor, coordenadas, tipo):
        self.cor = cor
        self.coordenadas = coordenadas
        self.tipo = tipo
        self.jogadas_possiveis = []

