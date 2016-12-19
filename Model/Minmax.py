from Node import *

class MinMax(object):
    def __init__(self):

        return

# Jogador definido como um inteiro, para representar quem joga atualmente... jogador == cor
#  esse valor ira ser multiplicado por -1  para calcular o valor do max player
    def minmax(self,node,jogador,profundidade):
        if(profundidade == 0):
            return self.avaliaTabuleiro(node.tabuleiro,jogador)*jogador
        valor = 0
        if(jogador > 0):  #maxplayer quer o maior valor dos filhos
            valor = (-1)*float("inf")
            aux =0
            for f in node.filhos:
                aux = self.minmax(f,-jogador,profundidade-1)
                if(aux > valor):
                    valor= aux
        else:
            for f in node.filhos:
                valor = float("inf")
                aux = 0
                for f in node.filhos:
                    aux = self.minmax(f,-jogador, profundidade - 1)
                    if (aux < valor)
                        valor = aux
        return valor




    #TODO: implementar avaliaTabuleiro
    # Heuristica escolhida: qtd de peças em jogo, i.e:peças do adversario - pecas do jogador
    def avaliaTabuleiro(self,tabuleiro,jogador):
         valor = 0  # inicia assumindo igualdade
         for p in tabuleiro.lista_das_brancas
             if(p.cor == jogador):
                 valor+=1
             else:
                 valor-=1

         for p in tabuleiro.lista_das_pretas
             if(p.cor == jogador):
                 valor+=1
             else:
                 valor-=1

         return valor