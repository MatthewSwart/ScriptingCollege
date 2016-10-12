from graphics import *

win = GraphWin("Square", 400, 400)

p = Point(350, 350)
p.draw(win)

rect = Rectangle(Point(50, 50), p)
rect.draw(win)
rect.setFill('yellow')

txt = Text(Point(200, 200), 'Hello World')
txt.draw(win)
txt.setFill('red')

win.getMouse()
