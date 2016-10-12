#!C:\Python27\python
board = []

class Blackpiece:
        inner_html = "<img src=\"p1.png\">"
        def __str__(self):
                return self.inner_html
                
def makeboard():
        
        line = []
        line1 = []
        line2 = []
        p1 = Blackpiece()
        p2 = Blackpiece()
        p3 = Blackpiece()
        p4 = Blackpiece()
        p5 = Blackpiece()
        p6 = Blackpiece()
        p7 = Blackpiece()
        p8 = Blackpiece()
        pieces = [p1, p2, p3, p4, p5, p6, p7, p8]
        for i in range(8):
                if i % 2:
                        line1.append("<br>")
                else:
                        line1.append(pieces[(i-1)/2])
        for i in range(8):
                if i % 2:
                        line2.append(pieces[(i+4)/2])
                else:
                        line2.append("<br>")
        board.append(line1)
        board.append(line2)
        for i in range(8):
                line.append("<br>")
        for i in range(2, 8):
                board.append(line)
        
        
        
def printboard():
	makeboard()
	s = ""
	print "<table>"
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
