'''
Created on May 10, 2014

@author: Scurvy
'''

import os, sys
import pygame
import default

from default.TileMap1 import *
from pygame.locals import *

windowWidth = 640
windowHeight = 480

tilesize = 32
scroll_buff = tilesize * 3

keys = [0,0,0,0] #List/Array declaration
black = (0,0,0) #Tuple declaration

"""
"""
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


"""
"""
if __name__ == '__main__':
	pygame.init()
	print("Initializing")
	
	screen = pygame.display.set_mode((windowWidth, windowHeight))
	map = TileMap1(tilesize, 30, 24)
	
	window_rect = pygame.Rect(0, 0, windowWidth, windowHeight)
	viewport_rect = window_rect.copy()
	background = pygame.Surface((map.mapWidth*tilesize, map.mapHeight*tilesize))
	
	player = pygame.image.load("human_m.png").convert()
	player_rect = pygame.Rect(200, 200, tilesize, tilesize)

	
	#THE ALMIGHTY GAME LOOP
	while 1:
		movement = [0,0]
		player_move = [0,0]
		view_move = [0,0]
		event_update()

		#determine if there is movement
		movement[0] = keys[0] + keys[1]
		movement[1] = keys[2] + keys[3]
		
		#moving left
		if movement[0] < 0 and player_rect.left > 0:
			if player_rect.left > scroll_buff or viewport_rect.left <= 0:
				player_move[0] = -1
			else:
				view_move[0] = -1
				
		#moving right
		if movement[0] > 0 and player_rect.right < map.drawWidth: 
			if player_rect.right < map.drawWidth-scroll_buff or viewport_rect.right >= map.drawWidth:
				player_move[0] = 1
			else:
				view_move[0] = 1
			
		#moving up
		if movement[1] < 0 and player_rect.top > 0:
			if player_rect.top > scroll_buff or viewport_rect.top <= 0:
				player_move[1] = -1
			else:
				view_move[1] = -1
				
		#mvoing down
		if movement[1] > 0 and player_rect.bottom < map.drawHeight: 
			if player_rect.bottom < map.drawHeight-scroll_buff or viewport_rect.bottom >= map.drawHeight:
				player_move[1] = 1
			else:
				view_move[1] = 1 
		
		#update viewport and return.
		viewport_rect = viewport_rect.move(view_move)
		player_rect = player_rect.move(player_move)

		screen.fill(black)
		for x in range(map.mapWidth):
			for y in range(map.mapHeight):
				tile = map.map[x][y]
				background.blit(tile, (x*tilesize, y*tilesize))
				
		viewport = background.subsurface(viewport_rect)
		screen.blit(viewport, window_rect)
		screen.blit(player, player_rect)
		pygame.display.flip() 
				


