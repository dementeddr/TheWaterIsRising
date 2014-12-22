'''
Created on May 10, 2014

@author: Scurvy
'''

import os, sys, math
import pygame

#This whole block of imports just... hurts. Get some packages up in here fool.
from TileMap1 import *
from TileMap2 import *
from World import *
from Entity import *
from Player import *

from pygame.locals import *

pygame.init()
print("Initializing")

window_size = (640, 480)

"""
"""
def event_update(world):
	#global window_sized
		
	#Update events
	for event in pygame.event.get():
		#On quit
		if event.type == pygame.QUIT:
			sys.exit()
		#On window resizing
		#elif event.type == VIDEORESIZE:
		#	window_sized = pygame.Rect(0,0, event.dict['w'], event.dict['h'])
		#	screen = pygame.display.set_mode(event.dict['size'],HWSURFACE|DOUBLEBUF|RESIZABLE)
		
		#update keyboard presses
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				world.keys[0] = 1;
			elif event.key == pygame.K_RIGHT:
				world.keys[1] = 1;
			elif event.key == pygame.K_UP:
				world.keys[2] = 1;
			elif event.key == pygame.K_DOWN:
				world.keys[3] = 1;
		#update keyboard releases
		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT:
				world.keys[0] = 0;
			elif event.key == pygame.K_RIGHT:
				world.keys[1] = 0;
			elif event.key == pygame.K_UP:
				world.keys[2] = 0;
			elif event.key == pygame.K_DOWN:
				world.keys[3] = 0;
				
	world.frame_number += 1
			
			
	
"""
"""
if __name__ == '__main__':

	screen = pygame.display.set_mode(window_size, HWSURFACE|DOUBLEBUF) #|RESIZEABLE)
	clock = pygame.time.Clock()
	black = (0,0,0) #Tuple declaration
		
	world = World(window_size)
	player = Player(world)

	for x in range(world.map.mapWidth):
		for y in range(world.map.mapHeight):
			tile = world.map.map[x][y][0]
			world.background.blit(tile, (x*world.tilesize, y*world.tilesize))
			
	#bgx2 = pygame.Surface((map.drawWidth*2, map.drawHeight*2))
	#pygame.transform.scale2x(background, bgx2)
	
	#THE ALMIGHTY GAME LOOP
	while 1:		
		event_update(world)
		player.movement_update(world)

		#print("Resize width: ", window_sized.width)
		#print("Resize height: ", window_sized.height)

		#w_ratio = window_sized.width // window_rect.width
		#h_ratio = window_sized.height // window_rect.height
		
		#bg_new_dim = (w_ratio*background.get_width(), h_ratio*background.get_height())
		
		#bg_new = pygame.Surface(bg_new_dim)
		#pygame.transform.scale(background, (bg_new_dim), bg_new)
		
		screen.fill(black)				
		viewport = world.background.subsurface(player.view_rect)
		screen.blit(viewport, world.window_rect)
		
		#Here we draw the player to the screen, using fancy math.
		screen.blit(player.sprite, pygame.Rect(player.ent_rect.left - player.view_rect.left, 
									player.ent_rect.top - player.view_rect.top,
									 world.tilesize,
									  world.tilesize))
		pygame.display.flip() 
		
		clock.tick(80)
				
