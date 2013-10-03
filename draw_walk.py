#draw_walk.py
# Simulates and draws a random walk of n steps

from graphics import *
from math import *
from random import random
from time import *

def main():
    printIntro()
    n, start = getInput()
    win = drawWin()
    drawWalk(n, start, win)
    win.getMouse()
    win.close()

def drawWin():
    win = GraphWin("Random walk", 600, 600)
    win.setCoords(-50, -50, 50, 50)
    return win

def drawWalk(n, start, win):
    for i in range(n):
        angle = random()*2*pi
        x = start.getX()
        y = start.getY()
        x = x + cos(angle)
        y = y + sin(angle)
        NewStart = Point(x,y)
        Line(start, NewStart).draw(win)
        start = NewStart
        sleep(0.005)

def getInput():
    n = input("How many steps should I take?: ")
    a, b = input("Where should I start? (x, y): ")
    start = Point(a, b)
    return n, start

def printIntro():
    print "This program simulates a random walk and draws"
    print "it on the screen given a number of steps and"
    print "a starting place"
    print

if __name__ == "__main__": main()
