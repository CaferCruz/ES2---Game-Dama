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
    jogo = regra.carregarJogo(sid)
    tab = jogo.tabuleiro
    
    tox = int(to[1])
    toy = int(to[2])
    
    frox = int(fro[1])
    froy = int(fro[2])

    pcode = 0 if pid[0] == 'w' else 1
    peca = Peca(pcode, (frox, froy), 0)

    res = regra.valida_mover(tabuleiro, Peca, (frox, froy), (tox, toy))

    if(res):
        estado, tabuleiro = regra.capsula(tabuleiro, Peca, (frox, froy), (tox, toy))
        tabuleiro = regra.capsula_atualiza(Peca, (tox, toy), tabuleiro)

        printboard(tabuleiro)

    else:
        print "0"
    

