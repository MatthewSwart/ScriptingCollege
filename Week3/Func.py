#Functions used for use later in program to build xmax tree

from graphics import *

def tri(win, x1, y1, x2, y2, x3, y3, shade='green'):
	tri1 = Polygon(Point(x1, y1),Point(x2, y2),Point(x3, y3))
	tri1.setFill(shade)
	tri1.draw(win)

def circ(win, x, y, rad, shade='black'):
	centre = Point(x, y)
	circ1 = Circle(centre, rad)
	circ1.setFill(shade)
	circ1.draw(win)

def main():

	win = GraphWin("Christmas", 200, 200)
	top = tri(win, 50, 175, 100, 125, 150, 175)
	mid = tri(win, 50, 145, 100, 95, 150, 145)
	bot = tri(win, 50, 115, 100, 65, 150, 115)
	firCric = circ(win, 100, 100, 5, 'yellow')	
	secCirc = circ(win, 90, 130, 5, 'red')
	thirdCirc = circ(win, 110, 160, 5, 'blue')
	rec = Rectangle(Point(90, 175), Point(110, 200))
	rec.setFill('black')
	rec.draw(win)
	mess = Text(Point(100, 25), 'Happy Xmas')
	mess.draw(win)
	win.getMouse()
	win.close()

if __name__ == '__main__':
	main()
