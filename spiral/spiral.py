#!/bin/env python2

"""
Identical elements are generated with a periodicity T at a given radius R0
from a center in a plane surface. They are radially advected at velocity V0, and
there is a repulsive interaction between them (so that the new element will
appear as far as possible from the preceding ones, i.e. in the largest available
place).

G = (V0 * T) / R0 = 0.15
"""

import math
from graphics import *
from pygame.locals import *
from time import sleep

def findBestPos(points, radius):
	bestAngle = 0
	bestPotential = 100000.0
	bestX = radius
	bestY = 0
	for angle in range(0, 360, 10):
		radians = math.radians(angle)
		x = radius * math.cos(radians)
		y = radius * math.sin(radians)
		potential = 0.0
		for point in points:
			potential += 1.0 / math.hypot(point.getP1().getX() - x, point.getP1().getY() - y);
		if potential < bestPotential:
			bestPotential = potential
			bestAngle = angle
			bestX = x
			bestY = y
	return Point(bestX, bestY)

velocity = 10
radius = 10
period = 0.15
points = []
winSize = 350

win = GraphWin("Spiral", winSize * 2, winSize * 2)
win.setCoords(-winSize, -winSize, winSize, winSize)
win.setBackground("tan")

while True:
	for circ in points:
		x = circ.getP1().getX()
		y = circ.getP1().getY()
		angle = math.atan2(y, x)
		realVelocity = velocity * (math.hypot(x, y) / radius)
		circ.move(velocity * math.cos(angle), velocity * math.sin(angle))
	
	newPos = findBestPos(points, radius)
	circ = Circle(newPos, 1.5)
	circ.setFill("green")
	circ.setOutline("green")
	circ.draw(win)
	points.append(circ)

	sleep(period)
