from graphics import *
from snowMan import *

def main():
	win = GraphWin('Home')
	roof = tri(win, 50, 100, 100, 50, 150, 100, 'green')
	win.getMouse()
	home = box(win, 50, 100, 150, 150, 'red')
	win.getMouse()
	door = box(win, 70, 120, 90, 150, 'black') 
	win.getMouse()
	wind = box(win, 115, 110, 130, 125, 'pink') 
	win.getMouse()
	sun = circ(win, 160, 70, 10, 'orange')
	win.getMouse()
	win.close()

if __name__ == '__main__':
	main()
