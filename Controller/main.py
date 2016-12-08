# Main conduz o jogo
from Minmax import *
from Tabuleiro import *

from Jogador import *
from Regras import *
from Peca import *
from Jogo import *

# Configura os tamanhos do tabuleiro
regras = Regras()

# Recebe o input do usuario
class Main(object):
    def get_jogada_usuario(t):

        #aviso1 = "Escolha uma peca sua para mover... " + chr(t.lista_das_brancas[0][0] + 97) + str(t.lista_das_brancas[0][1])
        print("aviso 1")
        while True: # Enquanto nao receber input valido
            jogada = []
            jogada = input().lower().split()
            if not(len(jogada) == 2):
                print ("Essa jogada nao e valida, tente novamente.", " aviso1")
                continue
            origem = (int(jogada[0][1]), ord(jogada[0][0]) - 97)
            peca = Peca(0,origem, 0)
            destino = (int(jogada[1][1]), ord(jogada[1][0]) - 97)

            # A peca movida pertence ao jogador?
            pertence = False
            for pecab in t.lista_das_brancas:
                if pecab.coordenadas == peca.coordenadas:
                    pertence = True
                    break

            if not (pertence):
                print ("peca: ", peca," esta dentro de ", t.lista_das_brancas)
                print ("Voce nao pertence a peca ", origem, ". Por favor, selecione uma das suas pecas.")#, t.lista_das_brancas
                continue
            break
        jogada = (peca, destino)
        return jogada


    def initJogo():
        while (True):
            print("Gostaria de abrir um jogo salvo? s/n")
            resp = raw_input().lower()

            if str(resp) == 's':
                j = regras.carregarJogo('save.json')
                j.tabuleiro.printa_tabuleiro()
                return j.tabuleiro
                break
            else:
                if str(resp) == 'n':
                    j = regras.novoJogo()
                    j.tabuleiro.printa_tabuleiro()
                    return j.tabuleiro
                    break

            print ("Escolha invalida, tente novamente")

    def salvarJogo(tabuleiro):
        while (True):
            print("Deseja salvar o jogo? s/n")
            resp = raw_input().lower()

            if str(resp) == 's':
                regras.salvarJogo(tabuleiro, "save.json")
                print("Jogo salvo com sucesso.")
                break
            else:
                if str(resp) == 'n':
                    break

            print ("Escolha invalida, tente novamente")

        return None

    ### MAIN  ###
    nome = "Lucas"
    print("######\tDamEX\t######")
    print("Comandos: Mover -> posInicio posDestino, ex: a1 b2")
    print("Comando: save")
    print("######################")

    tabuleiro = initJogo()

    # loop
    while regras.vitoria(tabuleiro) == -1:
        #salvarJogo(tabuleiro)
        # Usuario comeca jogando
        jogada_usuario = regras.mover(tabuleiro, 0)

        tabuleiro.printa_tabuleiro()


        # Segundo jogador / IA
        print ("Seu adversario ira jogar!")
        jogada_usuario = regras.mover(tabuleiro, 1)

        print ("~~~~~~~~~~~~JOGADA DO COMPUTADOR~~~~~~~~~~~~")
        tabuleiro.printa_tabuleiro()
        if regras.vitoria(tabuleiro) == 0:
            print ("Usuario ganhou o jogo")
            print ("Game Over")
            break
        elif regras.vitoria(tabuleiro) == 1:
            print ("Computador ganhou o jogo")
            print ("Game Over")
            break


