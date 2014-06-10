'''
Created on May 10, 2014

@author: Scurvy
'''

import pygame, sys
from pygame.locals import *


windowWidth = 640
windowHeight = 480

mapWidth = windowWidth // 32
mapHeight = windowHeight // 32

tilesize = 32

speed = [1, 1] #Array/List declaration
black = (0,0,0) #Tuple declaration

print(mapWidth) 
print(mapHeight)

def create_map():
	floor = pygame.image.load("rect_gray0.png")
	map = []
	for x in range(mapWidth):
		line = []
		map.append(line)
		for y in range(mapHeight):
			#tile = pygame.Rect(x*tilesize, y*tilesize, tilesize, tilesize)
			line.append(floor.subsurface((0,0,tilesize,tilesize)))
			
	return map
			

if __name__ == '__main__':

	pygame.init()
	print("Initializing")
	print('Path to pygame module:', pygame.__file__)
	
	screen = pygame.display.set_mode((windowWidth, windowHeight))
	map = create_map()
	
	while 1:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

		screen.fill(black)
						
		for x in range(mapWidth):
			for y in range(mapHeight):
				tile = map[x][y]
				#screen.blit(floor, tile)
				screen.blit(tile, (x*tilesize, y*tilesize))
				
		screen.display.flip() 
				


