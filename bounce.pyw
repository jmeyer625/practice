# bounce.pyw
# animates a circle bouncing around a window

from graphics import *
from time import sleep
from math import *

def main():

    win = GraphWin("Circle animation", 600, 600)
    dx = 1
    dy = 1
    circle = Circle(Point(30,30), 5)
    circle.draw(win)
    
    for i in range(10000):
        P2 = circle.getP2()
        P1 = circle.getP1()
        if P2.getX() == 600:
            dx = -1
        elif P1.getX() == 0:
            dx = 1
        else:
            dx = dx
        if P1.getY() == 600:
            dy = -1
        elif P2.getY() == 0:
            dy = 1
        else:
            dy = dy

        circle.move(dx,dy)
        sleep(0.005)

    win.getMouse()
    win.close()

main()
