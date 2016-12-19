from Node import *

class MinMax(object):
    def __init__(self):

        return



    def minmax(self,node,jogador,profundidade,turno):
        if(profundidade == 0):
            return self.avaliaTabuleiro(node.tabuleiro,jogador)*turno
        valor = 0
        if(turno > 0):  #maxplayer quer o maior valor dos filhos
            valor = (-1)*float("inf")
            aux =0
            for f in node.filhos:
                aux = self.minmax(f,jogador,profundidade-1,-turno)
                if(aux > valor):
                    valor= aux
        else:
            for f in node.filhos:
                valor = float("inf")
                aux = 0
                for f in node.filhos:
                    aux = self.minmax(f,jogador, profundidade - 1,-turno)
                    if (aux < valor):
                        valor = aux
        return valor




        def avaliaTabuleiro(self,tabuleiro,jogador):
         valor = 0  # inicia assumindo igualdade
         for p in tabuleiro.lista_das_brancas:
             if(p.cor == jogador):
                 valor+=1
             else:
                 valor-=1

         for p in tabuleiro.lista_das_pretas:
             if(p.cor == jogador):
                 valor+=1
             else:
                 valor-=1

         return valor