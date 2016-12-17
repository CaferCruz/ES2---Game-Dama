from Node import *

class MinMax(object):
    def __init__(self):
        return

# Jogador definido como um inteiro, para representar quem joga atualmente...
#  esse valor ira ser multiplicado por -1  para calcular o valor do max player
    def minmax(self,node,jogador,profundidade):
        if(profundidade == 0):
            return self.avaliaTabuleiro(node.tabuleiro)
        valor = 0
        if(jogador > 0):  #maxplayer quer o maior valor dos filhos
            valor = (-1)*float("inf")
            aux =0
            for f in node.filhos:
                aux = self.minmax(f,-jogador,profundidade-1)
                if(aux > valor)
                    valor= aux
        else:
            for f in node.filhos:
                valor = float("inf")
                aux = 0
                for f in node.filhos:
                    aux = self.minmax(f, -jogador, profundidade - 1)
                    if (aux < valor)
                        valor = aux
        return valor
    
    def avaliaTabuleiro(self,tabuleiro):
        return