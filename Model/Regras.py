def movimentosValidos(tabuleiro, jogador, casaOrigem, casaDestino):
    temQueComer = verificaSeTemQueComer(tabuleiro, jogador)
    if temQueComer:
        return maioresSequenciasDeComer(tabuleiro, jogador)

#cor  0 = branca
#cor  1 = preta
#tipo 0 = peça comum
#tipo 1 = peça preta
def verificaSeTemQueComer(tabuleiro, jogador):
    retorno = None
    if jogador.cor == 0:
        for peca in tabuleiro.lista_das_brancas:
            if peca.tipo == 0:
                if (peca.coordenadas[0] + 1, peca.coordenadas[1] - 1) in tabuleiro.lista_das_pretas and (peca.coordenadas[0] + 2, peca.coordenadas[1] - 1) :
                    return retorno



def maioresSequenciasDeComer(tabuleiro, jogador):
    return
# Regra de empate definida pelo grupo. 20 rodadas(1 rodada = 1 jogada preta e 1 jogada branca) sem ninguém comer ninguém
def empate(rodadasSemComer):
    if rodadasSemComer == 20:
        return True
    return False
# Verifica se alguém venceu. Se preto venceu, retorna 1. Se branco venceu, retorna 0. Se ninguém venceu, retorna -1.
def vitoria(tabuleiro):
    if(tabuleiro.lista_das_brancas.len == 0):
        return 1
    if (tabuleiro.lista_das_pretas.len == 0):
        return 0
    return -1
# Verifica se a peca que está sendo movida deve virar dama ou não.
def virarDama(peca, altura):
    if peca.tipo == 1:
        return False
    if peca.coordenadas[1] == 0 and peca.cor == 0:
        return True
    if peca.coordenadas[1] == altura and peca.cor == 1:
        return True
    return False


