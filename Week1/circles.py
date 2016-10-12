from graphics import *

win = GraphWin('Face Value', 200, 200)
p = Point(170, 170)
head = Rectangle(Point(30, 30), p)
head.draw(win)

p1 = Point(30, 100)
lEar = Rectangle(Point(15, 75), p1)
lEar.setFill('yellow')
lEar.draw(win)

p2 = Point(185, 100)
rEar = Rectangle(Point(170, 75), p2)
rEar.setFill('yellow')
rEar.draw(win)

lEye = Circle(Point(75, 85), 15)
lEye.setFill('blue')
lEye.draw(win)

rEye = Circle(Point(125, 85), 15)
rEye.setFill('blue')
rEye.draw(win)

p3 = Point(100, 125)
nose = Line(Point(100, 85), p3)
nose.draw(win)

mouth = Oval(Point(75, 135), Point(125, 150))
mouth.setFill('black')
mouth.setOutline('red')
mouth.draw(win)



win.getMouse()
