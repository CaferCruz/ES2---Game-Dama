#!C:\Python27\python
board = []

class Blackpiece:
        inner_html = "<img src=\"p1.png\">"
        def __str__(self):
                return self.inner_html

class Whitepiece:
        inner_html = "<img src=\"p2.png\">"
        def __str__(self):
                return self.inner_html
                
def makeboard():
        
        line = []
        line0 = []
        line1 = []
        line2 = []
        line5 = []
        line6 = []
        line7 = []
        p1 = Blackpiece()
        p2 = Blackpiece()
        p3 = Blackpiece()
        p4 = Blackpiece()
        p5 = Blackpiece()
        p6 = Blackpiece()
        p7 = Blackpiece()
        p8 = Blackpiece()
        p9 = Blackpiece()
        pa = Blackpiece()
        pb = Blackpiece()
        pc = Blackpiece()
        w1 = Whitepiece()
        w2 = Whitepiece()
        w3 = Whitepiece()
        w4 = Whitepiece()
        w5 = Whitepiece()
        w6 = Whitepiece()
        w7 = Whitepiece()
        w8 = Whitepiece()
        w9 = Whitepiece()
        wa = Whitepiece()
        wb = Whitepiece()
        wc = Whitepiece()
        pieces = [p1, p2, p3, p4, p5, p6, p7, p8, p9, pa, pb, pc]
        wpieces = [w1, w2, w3, w4, w5, w6, w7, w8, w9, wa, wb, wc]
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

def main():
        header()
        print "<body>"
        printboard()
        print "</body>"
        print "</HTML>"
        
main()
#printboard()
