'''
Created on May 10, 2014

@author: Scurvy
'''

import pygame, sys
from pygame.locals import *

pygame.init()
print("Initializing")

windowWidth = 640
windowHeight = 480
windowSize = windowWidth, windowHeight

mapWidth = windowWidth // 32
mapHeight = windowHeight // 32

speed = [1, 1] #Array/List declaration
black = (0,0,0) #Tuple declaration

print(mapWidth) 
print(mapHeight)

screen = pygame.display.set_mode(windowSize)

axe = pygame.image.load("battle_axe2.png")
axeRect = axe.get_rect()

floor = pygame.image.load("rect_gray0.png")
#floorRects = [[floor.get_rect() for i in range(mapHeight)] for j in range(mapWidth)]
# = floor.get_rect()

while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
			
	axeRect = axeRect.move(speed)
	if axeRect.left < 0 or axeRect.right > windowWidth:
		speed[0] = -speed[0]
	if axeRect.top < 0 or axeRect.bottom > windowHeight:
		speed[1] = -speed[1]
		
	screen.fill(black)
	screen.blit(axe, axeRect)
	
	floorRects = []
	
	for x in range(0, mapWidth-1):
		line = []
		floorRects.append(line)
		for y in range(0, mapHeight-1):
			#print(x,y)
			#floorRects[x][y].move_ip(x*32, y*32)
			#screen.blit(floor, floorRects[x][y])
			rect = (x*32, x*32, 32, 32)
			line.append(floor.subsurface(rect))
	
	for x, row in enumerate(floorRects):
		for y, tile in enumerate(row):
			screen.blit(tile, (x*32, y*32))
	
	pygame.display.flip()
	
