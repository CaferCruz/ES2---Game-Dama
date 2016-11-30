# Main conduz o jogo
from Model.Minmax import *
from Model.Tabuleiro import *
from Model.Jogo import *
from Model.Jogador import *
from Model.Regras import *

# Configura os tamanhos do tabuleiro
largura = 8
altura = 8
primeiroJogador = 0

# Recebe o input do usuario

def get_jogada_usuario(t):

    aviso1 = "Escolha uma peca sua para mover... " + chr(t.lista_das_brancas[0][0] + 97) + str(t.lista_das_brancas[0][1])
    print(aviso1)
    while True: # Enquanto nao receber input valido
        jogada = []
        jogada = raw_input().lower().split()
        if not(len(jogada) == 2):
            print "Essa jogada nao e valida, tente novamente.", aviso1
            continue
        origem = (int(jogada[0][1]), ord(jogada[0][0]) - 97)
        peca = Peca(0,origem)
        destino = (int(jogada[1][1]), ord(jogada[1][0]) - 97)
        # A peca movida pertence ao jogador?
        if not (origem in t.lista_das_brancas):
            print "Voce nao pertence a peca ", origem, ". Por favor, selecione uma das suas pecas.", t.whitelist
            continue
        break
    jogada = (peca, destino)
    return jogada

### MAIN  ###

tabuleiro = Tabuleiro(largura, altura, primeiroJogador)
jogador1 = Jogador(tabuleiro.lista_das_brancas, "Lucas")
jogador2 = Jogador(tabuleiro.lista_das_pretas)
jogo = Jogo(jogador1, jogador2, tabuleiro)
tabuleiro.printa_tabuleiro()
print("DamEX")

# loop
while Regras.vitoria() == -1:
    # Usuario comeca jogando
    jogada_usuario = get_jogada_usuario(tabuleiro)
    try:
        jogador1.moverPecas(tabuleiro, jogada_usuario[0], jogada_usuario[1])
    except Exception:
        print "Jogada invalida"
        continue

    # Vez da maquina
    print "Vez do computador: computador pensando..."
    temp = minMax2(tabuleiro)
    tabuleiro = temp[0]
    print "~~~~~~~~~~~~JOGADA DO COMPUTADOR~~~~~~~~~~~~"
    tabuleiro.printa_tabuleiro()
    if Regras.vitoria(tabuleiro) == 0:
        print "Usuario ganhou o jogo"
        print "Game Over"
        break
    elif Regras.vitoria(tabuleiro) == 1:
        print "Computador ganhou o jogo"
        print "Game Over"
        break
    elif Regras.empate(rodadasSemComer):
        print "Empatou"
        print "Game Over"
        break

