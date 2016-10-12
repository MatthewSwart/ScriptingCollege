from graphics import *

win = GraphWin("Target practice", 400, 400)
centre = Point(200, 200)
centre.draw(win)

#win.getMouse()

tar1 = Circle(Point(200, 200), 100)
tar1.setFill("white")
tar1.draw(win)
win.getMouse()

tar2 = Circle(Point(200, 200), 80)
tar2.setFill("black")
tar2.draw(win)
win.getMouse()

tar3 = Circle(Point(200, 200), 60)
tar3.setFill("red")
tar3.draw(win)
win.getMouse()

tar4 = Circle(Point(200, 200), 40)
tar4.setFill("blue")
tar4.draw(win)
win.getMouse()

tar5 = Circle(Point(200, 200), 20)
tar5.setFill("yellow")
tar5.draw(win)
win.getMouse()
