#!/usr/bin/env python

from Regras import *
from Jogo import *
from Jogador import *
from Tabuleiro import *
from Peca import *
from Visual import *
import cgi
import cgitb; cgitb.enable()

form = cgi.FieldStorage()
to = ""
fro = ""
pid = ""
sid = ""
works = 0

try:
    to = form.getvalue("to")
    fro = form.getvalue("from")
    sid = form.getvalue("id")
    pid = form.getvalue("this")
    works = 1
except:
    to = ""
    fro = ""
    sid = ""
    pid = ""
    works = -1

if(works > 0):
    regra = Regras()
    visual = Visual()
    jogo = regra.carregarJogo(sid)
    #jogo = regra.carregarJogo("150659578876257975456580117709407753831")
    tab = jogo.tabuleiro
    
    tox = int(to[1])
    toy = int(to[2])
    #tox, toy = 4, 2
    
    frox = int(fro[1])
    froy = int(fro[2])
    #frox, froy = 5, 3

    pcode = 0 if (pid[0] == 'w' or pid[0] == 'q') else 1
    #pcode = 0

    ptype = 0 if (pid[0] == 'd' or pid[0] == 'q') else 1
    #ptype = 0

    peca = Peca(pcode, (froy, frox), ptype)

    res = regra.validador(tab, peca, (froy, frox), (toy, tox))

    #print to, fro, sid, pid

    if(res):
        tab, estado = regra.capsula(tab, peca, (froy, frox), (toy, tox))
        p, tab = regra.capsula_atualiza(peca, (toy, tox), tab)
        peca.coordenadas = p.coordenadas
        if(not regra.nova_jogada(tab, peca, estado)):
            #Inserir a jogada da IA aqui. Retornar o tabuleiro atualizado
            #tab =
            visual.printboard(tab)
            regra.salvarJogo(tab, sid)
        else:
            visual.printboard(tab)
            regra.salvarJogo(tab, sid)

    else:
        print "0"
    

