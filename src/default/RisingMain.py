'''
Created on May 10, 2014

@author: Scurvy
'''

import os, sys
import pygame
from pygame.locals import *

windowWidth = 640 * 2
windowHeight = 480 * 2

#mapWidth = windowWidth // 32
#mapHeight = windowHeight // 32
mapWidth = 24
mapHeight = 20

tilesize = 32

speed = [1, 1] #Array/List declaration
black = (0,0,0) #Tuple declaration

print(mapWidth) 
print(mapHeight)

def create_map1():
	floor = pygame.image.load("rect_gray0.png").convert()
	map = []
	for x in range(mapWidth):
		line = []
		map.append(line)
		for y in range(mapHeight):
			#tile = pygame.Rect(x*tilesize, y*tilesize, tilesize, tilesize)
			line.append(floor.subsurface((0,0,tilesize,tilesize)))
			
	return map
			
			
def create_map2():
	floor1 = pygame.image.load("rect_gray0.png").convert()
	floor2 = pygame.image.load("floor_vines0.png").convtert()
	map = []
	for x in range(mapWidth):
		line = []
		map.append(line)
		for y in range(mapHeight):
			if y == 0 or y == mapHeight-1 or x == 0 or x == mapWidth-1:
				line.append(floor2.subsurface((0,0,tilesize,tilesize)))
			else:
				line.append(floor1.subsurface((0,0,tilesize,tilesize)))
			
	return map


if __name__ == '__main__':

	pygame.init()
	print("Initializing")
	
	screen = pygame.display.set_mode((windowWidth, windowHeight))
	tile_map = create_map2()
	map = pygame.Surface((mapWidth*tilesize, mapHeight*tilesize))
	window_rect = pygame.Rect(0, 0, windowWidth, windowHeight)
	viewport_rect = window_rect.copy()
	
	#THE ALMIGHTY GAME LOOP
	while 1:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

		screen.fill(black)
						
		for x in range(mapWidth):
			for y in range(mapHeight):
				tile = tile_map[x][y]
				map.blit(tile, (x*tilesize, y*tilesize))
				
		viewport = map.subsurface(viewport_rect)
		screen.blit(viewport, window_rect)
		pygame.display.flip() 
				


