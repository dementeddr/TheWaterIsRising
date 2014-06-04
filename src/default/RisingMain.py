'''
Created on May 10, 2014

@author: Scurvy
'''

import pygame, sys
from pygame.locals import *


windowWidth = 640
windowHeight = 480
windowSize = windowWidth, windowHeight

mapWidth = windowWidth // 32
mapHeight = windowHeight // 32

speed = [1, 1] #Array/List declaration
black = (0,0,0) #Tuple declaration

print(mapWidth) 
print(mapHeight)

def create_uniform_map():
	
	map = []
	for x in range(mapHeight):
		map.append([])
		for y in range(mapWidth):
			map[x].append(1)
			
	return map 

if __name__ == '__main__':

	pygame.init()
	print("Initializing")
	screen = pygame.display.set_mode(windowSize)

	screen.fill(black)

	map = create_uniform_map()
	
	for x in range(mapHeight):
		print()
		for y in range(mapWidth):
			print(map[x][y], end=" ")
	



