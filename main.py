#!C:\Python27\python
board = []
class Piece:
        inner_html = ""
        def __init__(self, value):
                self.inner_html = value
        def __str__(self):
                return self.inner_html
        
class Blackpiece(Piece):
        def __init__(self):
                Piece.__init__(self, "<img src=\"p1.png\">")

class Whitepiece(Piece):
        def __init__(self):
                Piece.__init__(self, "<img src=\"p2.png\">")
                
def makeboard():
        
        line = []
        line0 = []
        line1 = []
        line2 = []
        line5 = []
        line6 = []
        line7 = []
        pieces = [Blackpiece() for i in range(12)]
        wpieces = [Whitepiece() for i in range(12)]
        for i in range(8):
                if i % 2:
                        line0.append(pieces[(i-1)/2])
                        line6.append(wpieces[(i-1)/2])
                        line2.append(pieces[(i+7)/2])
                else:
                        line0.append("<br>")
                        line2.append("<br>")
                        line6.append("<br>")
        for i in range(8):
                if i % 2:
			line1.append("<br>")
			line5.append("<br>")
			line7.append("<br>")
                else:
			line1.append(pieces[(i+4)/2])
			line5.append(wpieces[(i+8)/2])
                        line7.append(wpieces[(i+4)/2])
        board.append(line0)
        board.append(line1)
        board.append(line2)
        for i in range(8):
                line.append("<br>")
        for i in range(3, 5):
                board.append(line)
        board.append(line5)
        board.append(line6)
        board.append(line7)
        
        
        
def printboard():
	makeboard()
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
			print "<td class=%s>" % s
			print board[n][x]
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
	print "<link rel=\"stylesheet\" type=\"text/css\" href=\"style.css\">"
	print "</head>"

def input_button(text):
        print "<input type=\"button\" name=\"%s\" value=\"%s\">" % (text, text) 

def main():
        header()
        print "<body>"
        print "<h1>DamEx</h1>"
        printboard()
        print "<form>"
        input_button("Novo Jogo")
        input_button("Salvar Jogo")
        input_button("Carregar Jogo")
        print "</form>"
        print "</body>"
        print "</HTML>"
        
main()
#printboard()
