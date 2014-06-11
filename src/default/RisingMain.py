'''
Created on May 10, 2014

@author: Scurvy
'''

import os, sys
import pygame
from pygame.locals import *

windowWidth = 640
windowHeight = 480

tilesize = 32

#mapWidth = windowWidth // 32
#mapHeight = windowHeight // 32
mapWidth = 30
mapHeight = 20

keys = [0,0,0,0] #List/Array declaration
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
	floor2 = pygame.image.load("floor_vines0.png").convert()
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


def event_update():
	#Update events
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		#update keyboard presses
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				keys[0] -= 1;
			elif event.key == pygame.K_RIGHT:
				keys[1] += 1;
			elif event.key == pygame.K_UP:
				keys[2] -= 1;
			elif event.key == pygame.K_DOWN:
				keys[3] += 1;
			print("keyboard: ", keys[0], " ", keys[1])
		#update keyboard releases
		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT:
				keys[0] += 1;
			elif event.key == pygame.K_RIGHT:
				keys[1] -= 1;
			elif event.key == pygame.K_UP:
				keys[2] += 1;
			elif event.key == pygame.K_DOWN:
				keys[3] -= 1;
			print("keyboard: ", keys[0], " ", keys[1])


def update(viewport_rect):	
	speed = [0,0]
	event_update()
	
	#determine if there is movement
	speed[0] = keys[0] + keys[1]
	speed[1] = keys[2] + keys[3]
	if viewport_rect.left <= 0 and keys[0] < 0:
		speed[0] = 0   
	if viewport_rect.right >= mapWidth*tilesize and keys[1] > 0:
		speed[0] = 0
	if viewport_rect.top <= 0 and keys[2] < 0:
		speed[1] = 0
	if viewport_rect.bottom >= mapHeight*tilesize and keys[3] > 0:
		speed[1] = 0 
		
	#update viewport and return.
	viewport_rect = viewport_rect.move(speed)
	return viewport_rect


if __name__ == '__main__':
	pygame.init()
	print("Initializing")
	
	screen = pygame.display.set_mode((windowWidth, windowHeight))
	
	tile_map = create_map2()
	window_rect = pygame.Rect(0, 0, windowWidth, windowHeight)
	viewport_rect = window_rect.copy()
	map = pygame.Surface((mapWidth*tilesize, mapHeight*tilesize))
	
	#THE ALMIGHTY GAME LOOP
	while 1:
		viewport_rect = update(viewport_rect)

		screen.fill(black)
		for x in range(mapWidth):
			for y in range(mapHeight):
				tile = tile_map[x][y]
				map.blit(tile, (x*tilesize, y*tilesize))
				
		viewport = map.subsurface(viewport_rect)
		screen.blit(viewport, window_rect)
		pygame.display.flip() 
				


