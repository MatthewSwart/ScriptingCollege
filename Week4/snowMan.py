from graphics import *

def tri(win, x1, y1, x2, y2, x3, y3, shade='green'):
	tri1 = Polygon(Point(x1, y1),Point(x2, y2),Point(x3, y3))
	tri1.setFill(shade)
	tri1.draw(win)

def box(win, x1, y1, x2, y2, shade='black'):
	rec = Rectangle(Point(x1, y1), Point(x2, y2))
	rec.setFill(shade)
	rec.draw(win)

def circ(win, x, y, rad, shade='black'):
	centre = Point(x, y)
	circ1 = Circle(centre, rad)
	circ1.setFill(shade)
	circ1.draw(win)

def lin(win, x1, y1, x2, y2, shade='black'):
	line1 = Line(Point(x1, y1), Point(x2, y2))
	line1.setFill(shade)
	line1.draw(win)

def main():
	win = GraphWin("Snowman")
	head = circ(win, 100, 60, 20, 'white')
	middle = circ(win, 100, 105, 25, 'white')
	base = circ(win, 100, 165, 35, 'white')
	eye = circ(win, 105, 50, 3)
	nose = tri(win, 115, 50, 140, 60, 115, 65, 'orange')
	mouth = lin(win, 105, 65, 115, 70)
	arm = lin(win, 100, 105, 160, 105)
	finger1 = lin(win, 150, 105, 160, 100)
	finger2 = lin(win, 150, 105, 160, 110)
	topHat = box(win, 90, 20, 110, 45)
	botHat = box(win, 80, 40, 120, 45)
	mess = Text(Point(100, 10), 'Season Greetings')
	mess.draw(win)
	win.getMouse()
	win.close()

if __name__ == '__main__':
	main()
	
