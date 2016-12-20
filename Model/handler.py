#!C:\Python27\python

from Regras import *
from Jogo import *
from Jogador import *
from Tabuleiro import *
from Peca import *
from main import *
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
    #jogo = regra.carregarJogo(sid)
    jogo = regra.carregarJogo("150659578876257975456580117709407753831")
    tab = jogo.tabuleiro
    
    #tox = int(to[1])
    #toy = int(to[2])
    tox, toy = 0, 1
    
    #frox = int(fro[1])
    #froy = int(fro[2])
    frox, froy = 2, 1

    #pcode = 0 if pid[0] == 'w' else 1
    pcode = 0
    peca = Peca(pcode, (frox, froy), 0)

    res = regra.validador(tab, Peca, (frox, froy), (tox, toy))

    print to, fro, sid, pid

    if(res):
        estado, tab = regra.capsula(tab, Peca, (frox, froy), (tox, toy))
        tab = regra.capsula_atualiza(Peca, (tox, toy), tab)

        printboard(tabuleiro)

    else:
        print "0"
    

