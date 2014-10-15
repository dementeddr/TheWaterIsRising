'''
Created on May 10, 2014

@author: Scurvy
'''

import os, sys
import pygame
import default

from default.TileMap1 import *
from pygame.locals import *

windowSize = (640, 480)

tilesize = 32
scroll_buff = tilesize * 3

keys = [0,0,0,0] #List/Array declaration
black = (0,0,0) #Tuple declaration

pygame.init()
print("Initializing")

screen = pygame.display.set_mode(windowSize, HWSURFACE|DOUBLEBUF|RESIZABLE)
clock = pygame.time.Clock()
map = TileMap1(tilesize, 30, 24)

window_rect = pygame.Rect(0, 0, windowSize[0], windowSize[1])
view_rect = window_rect.copy()
window_sized = window_rect.copy()
background = pygame.Surface((map.mapWidth*tilesize, map.mapHeight*tilesize))

player = pygame.image.load("human_m.png").convert()
player_rect = pygame.Rect(200, 200, tilesize, tilesize) #Starting location

	
"""
"""
def event_update():
	global keys
	global screen
	global window_sized
	
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
				keys[0] -= 1;
			elif event.key == pygame.K_RIGHT:
				keys[1] += 1;
			elif event.key == pygame.K_UP:
				keys[2] -= 1;
			elif event.key == pygame.K_DOWN:
				keys[3] += 1;
		#update keyboard releases
		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT:
				keys[0] = 0;
			elif event.key == pygame.K_RIGHT:
				keys[1] = 0;
			elif event.key == pygame.K_UP:
				keys[2] = 0;
			elif event.key == pygame.K_DOWN:
				keys[3] = 0;
			
			
"""
"""
def movement_update():
	global player_rect
	global view_rect
	global scroll_buff
	
	movement = [0,0]
	player_move = [0,0]
	view_move = [0,0]
	speed = 3
	
	#determine if there is movement
	movement[0] = keys[0] + keys[1]
	movement[1] = keys[2] + keys[3]
		
	#moving left
	if movement[0] < 0:
		if (player_rect.left > scroll_buff or player_rect.left <= scroll_buff
			and view_rect.left <= 0 and player_rect.left > 0):
			
			player_move[0] = -speed
		elif view_rect.left > 0:
			view_move[0] = -speed
			
	#moving right
	if movement[0] > 0:
		if (player_rect.right < view_rect.width - scroll_buff 
			or player_rect.right >= view_rect.width - scroll_buff 
			and view_rect.right >= map.drawWidth 
			and player_rect.right < view_rect.width):
			
			player_move[0] = speed
		elif view_rect.right < map.drawWidth:
			view_move[0] = speed
				
	#moving up
	if movement[1] < 0:
		if (player_rect.top > scroll_buff or player_rect.top <= scroll_buff
			and view_rect.top <= 0 and player_rect.top > 0):
				
			player_move[1] = -speed
		elif view_rect.top > 0:
			view_move[1] = -speed
				
	#moving down
	if movement[1] > 0:
		if (player_rect.bottom < view_rect.height - scroll_buff 
			or player_rect.bottom >= view_rect.height - scroll_buff 
			and view_rect.bottom >= map.drawHeight 
			and player_rect.bottom < view_rect.height):
			
			player_move[1] = speed
		elif view_rect.bottom < map.drawHeight:
			view_move[1] = speed
		
	#update viewport and player and return.
	view_rect = view_rect.move(view_move)
	player_rect = player_rect.move(player_move)
	
	
"""
"""
if __name__ == '__main__':

	for x in range(map.mapWidth):
		for y in range(map.mapHeight):
			tile = map.map[x][y]
			background.blit(tile, (x*tilesize, y*tilesize))
			
	#bgx2 = pygame.Surface((map.drawWidth*2, map.drawHeight*2))
	#pygame.transform.scale2x(background, bgx2)
	
	#THE ALMIGHTY GAME LOOP
	while 1:		
		event_update()
		movement_update()

		#print("Resize width: ", window_sized.width)
		#print("Resize height: ", window_sized.height)

		w_ratio = window_sized.width // window_rect.width
		h_ratio = window_sized.height // window_rect.height
		
		bg_new_dim = (w_ratio*background.get_width(), h_ratio*background.get_height())
		
		bg_new = pygame.Surface(bg_new_dim)
		pygame.transform.scale(background, (bg_new_dim), bg_new)
		
		screen.fill(black)				
		viewport = background.subsurface(view_rect)
		screen.blit(viewport, window_rect)
		screen.blit(player, player_rect)
		pygame.display.flip() 
		
		clock.tick(80)
				
