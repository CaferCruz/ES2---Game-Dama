import copy

class Piece:
        inner_html = ""
        def __init__(self, value):
                self.inner_html = value
        def __str__(self):
                return self.inner_html
        
class Blackpiece(Piece):
        def __init__(self, id):
                Piece.__init__(self, "<img src=\"..\images\p1.png\" id=\"b%d\" draggable=\"true\" ondragstart=\"drag(event)\">" % id)

class Blackdama(Piece):
        def __init__(self, id):
                Piece.__init__(self, "<img src=\"..\images\d1.png\" id=\"d%d\" draggable=\"true\" ondragstart=\"drag(event)\">" % id)

class Whitedama(Piece):
        def __init__(self, id):
                Piece.__init__(self, "<img src=\"..\images\d2.png\" id=\"q%d\" draggable=\"true\" ondragstart=\"drag(event)\">" % id)

class Whitepiece(Piece):
        def __init__(self, id):
                Piece.__init__(self, "<img src=\"..\images\p2.png\" id=\"w%d\" draggable=\"true\" ondragstart=\"drag(event)\">" % id)

class Visual(object):
                    
    def makeboard(self, tab):
            
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
                    board[x][y] = Blackdama(c) if p.tipo else Blackpiece(c)

            for c, p in enumerate(tab.lista_das_brancas):
                    (x, y) = p.coordenadas[0], p.coordenadas[1]
                    board[x][y] = Whitedama(c) if p.tipo else Whitepiece(c)

            return board
                    
            
            
            
    def printboard(self, tab):
            board = self.makeboard(tab)
            s = ""
            #print "<table frame=\"box\">"
            print "<tbody>"
            for n in range(8):
                    print "<tr>"
                    for x in range(8):
                            if n % 2:
                                    s = "a" if x % 2 else "b"
                            else:
                                    s = "b" if x % 2 else "a"
                            print "<td class=\"%s\" id=\"p%d%d\" ondrop=\"drop(event)\" ondragover=\"allowDrop(event)\">" % (s, n, x)
                            #print "(%d, %d)" % (n, x)
                            print board[x][n]
                            print "</td>"
                    print "</tr>"
            print "</tbody>"
            #print "</table>"
