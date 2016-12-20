#!/usr/bin/env python

from Tabuleiro import *
from Peca import *
from Regras import *
from Jogo import *
from Visual import *
import copy
import uuid
import cgi
import cgitb; cgitb.enable()

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
        visual = Visual()
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
        print  "<script src=\"..\css\script.js\"></script>"
        print "<table frame=\"box\" id=\"main\">"
        visual.printboard(tabuleiro)
        print "</table>"
        print "<form>"
        input_button("Novo Jogo")
        input_button("Salvar Jogo")
        input_button("Carregar Jogo")
        print "<input type=\"hidden\" id=\"sid\" name=\"input1\" value=\"%d\" />" % sess_id.int
        print "</form>"
        print "</body>"
        print "</HTML>"
        
main()
#printboard()
