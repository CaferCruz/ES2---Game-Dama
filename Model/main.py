#!python27
#!C:\Python27\python

from Tabuleiro import *
from Peca import *
from Regras import *
from Jogo import *
import copy
import uuid
import cgi
import cgitb; cgitb.enable()

class Piece:
        inner_html = ""
        def __init__(self, value):
                self.inner_html = value
        def __str__(self):
                return self.inner_html
        
class Blackpiece(Piece):
        def __init__(self, id):
                Piece.__init__(self, "<img src=\"..\images\p1.png\" id=\"b%d\">" % id)

class Whitepiece(Piece):
        def __init__(self, id):
                Piece.__init__(self, "<img src=\"..\images\p2.png\" id=\"w%d\">" % id)
                
def makeboard(tab):
        
        line = []
        line0 = []
        line1 = []
        line2 = []
        line3 = []
        line4 = []
        line5 = []
        line6 = []
        line7 = []
        board = [line0, line1, line2, line3, line4, line5, line6, line7]

        for i in range(8):
                line.append("<br>")
        
        for i in range(8):
                board[i] = copy.deepcopy(line)

        #tabuleiro = Tabuleiro(8, 8)
                
        for c, p in enumerate(tab.lista_das_pretas):
                (x, y) = p.coordenadas[0], p.coordenadas[1]
                board[x][y] = Blackpiece(c)

        for c, p in enumerate(tab.lista_das_brancas):
                (x, y) = p.coordenadas[0], p.coordenadas[1]
                board[x][y] = Whitepiece(c)

        return board
                
        
        
        
def printboard(tab):
        board = makeboard(tab)
        s = ""
        print "<table frame=\"box\">"
        print "<tbody>"
        for n in range(8):
                print "<tr>"
                for x in range(8):
                        if n % 2:
                                s = "a" if x % 2 else "b"
                        else:
                                s = "b" if x % 2 else "a"
                        print "<td class=\"%s\" id=\"p%d%d\">" % (s, n, x)
                        #print "(%d, %d)" % (n, x)
                        print board[x][n]
                        print "</td>"
                print "</tr>"
        print "</tbody>"
        print "</table>"

def header():
        print "<!DOCTYPE html>"
        print "<HTML>"
        print "<head>"
        print "<meta content=\"text/html; charset=UTF-8\" http-equiv=\"content-type\">"
        print "<title>Checkers EX2</title>"
        print "<link rel=\"stylesheet\" type=\"text/css\" href=\"..\css\style.css\">"
        print "</head>"

def input_button(text):
        print "<input type=\"button\" name=\"%s\" value=\"%s\">" % (text, text) 

def main():
        form = cgi.FieldStorage()
        input1 = ""
        sess_id = -1
        tabuleiro = Tabuleiro(8, 8)
        regras = Regras()
        try:
                input1 = form1.getvalue("input1")
                sess_id = int(input1)
        except:
                sess_id = -1
        if sess_id <0:
                sess_id = uuid.uuid4()
                Regras.salvarJogo(regras, tabuleiro, str(sess_id.int))
        else:
                jogo = carregarJogo(regras, str(sess_id.int))
                tabuleiro = jogo.tabuleiro
        header()
        print "<body>"
        print "<h1>DamEx</h1>"
        printboard(tabuleiro)
        print "<form>"
        input_button("Novo Jogo")
        input_button("Salvar Jogo")
        input_button("Carregar Jogo")
        print "<input type=\"hidden\" name=\"input1\" value=\"%d\" />" % sess_id.int
        print "</form>"
        print "</body>"
        print "</HTML>"
        
main()
#printboard()
