'''
Created on May 10, 2014

@author: Scurvy
'''

import os, sys, math
import pygame

from TileMap1 import *
from pygame.locals import *

windowSize = (640, 480)

tilesize = 32
scroll_buff = tilesize * 5
on_ground = False
speed = 3
jump_speed = 8

keys = [0,0,0,0] #List/Array declaration
black = (0,0,0) #Tuple declaration

pygame.init()
print("Initializing")

screen = pygame.display.set_mode(windowSize, HWSURFACE|DOUBLEBUF) #|RESIZEABLE)
clock = pygame.time.Clock()
map = TileMap1(tilesize, 30, 24)

window_rect = pygame.Rect(0, 0, windowSize[0], windowSize[1])
view_rect = window_rect.copy()
window_sized = window_rect.copy()
background = pygame.Surface((map.mapWidth*tilesize, map.mapHeight*tilesize))

player = pygame.image.load("human_m.png").convert()
player_rect = pygame.Rect(200, 100, tilesize, tilesize) #Starting location
player_move = [0,0]

frame_number = 0


"""
"""
def event_update():
	global keys
	global screen
	global window_sized
	global frame_number
	
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
				keys[0] = 1;
			elif event.key == pygame.K_RIGHT:
				keys[1] = 1;
			elif event.key == pygame.K_UP:
				keys[2] = 1;
			elif event.key == pygame.K_DOWN:
				keys[3] = 1;
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
				
	frame_number += 1
			
			
"""
"""
def movement_update():
	global player_rect
	global view_rect
	global scroll_buff
	global speed
	global on_ground
	global player_move
	global frame_number
	
	view_move = [0,0]
	movement = [0,0]
	
	#determine if there is movement
	movement[0] = keys[1] - keys[0]
	if on_ground == True: 
		if keys[2] == 1:
			player_move[1] = -jump_speed
			movement[1] = -1
		else:
			player_move[1] = 1 
			movement[1] = 1
	# if on the ground, player should try to move down
	elif on_ground == False:
		movement[1] = player_move[1]
		if frame_number % 6 == 0:
			player_move[1] += 1 #accelerate towards ground
			
	if movement[0] > 0:
		player_move[0] = speed
	elif movement[0] < 0:
		player_move[0] = -speed
	else:
		player_move[0] = 0
		
	player_move = collision_detect(player_rect, player_move)

		
	#moving left
	if movement[0] < 0:
		if (player_rect.left > 0):
			if (player_rect.left < -player_move[0]):
				player_move[0] = -player_rect.left
			#else:
				#player_move[0] = -speed
		#move the viewport		
		if (player_rect.left < view_rect.left + scroll_buff and view_rect.left > 0):
			if (view_rect.left < -player_move[0]):
				view_move[0] = -view_rect.left
			else:
				view_move[0] = player_move[0]
		
	#moving right
	if movement[0] > 0:
		if (player_rect.right < background.get_width()):
			if (background.get_width() - player_rect.right < player_move[0]):
				player_move[0] = background.get_width() - player_rect.right
			#else:
				#player_move[0] = speed
		#move the viewport		
		if (player_rect.right > view_rect.right - scroll_buff and view_rect.right < background.get_width()):
			if (background.get_width() - view_rect.right < player_move[0]):
				view_move[0] = background.get_width() - view_rect.right
			else:
				view_move[0] = player_move[0]
				
	#moving up
	if movement[1] < 0:
		if (player_rect.top > 0):
			if (player_rect.top < player_move[1]):
				player_move[1] = -player_rect.top
			#else:
				#player_move += 1 

		#move the viewport		
		if (player_rect.top < view_rect.top + scroll_buff and view_rect.top > 0):
			if (view_rect.top < -player_move[1]):
				view_move[1] = -view_rect.top
			else:
				view_move[1] = player_move[1]
		
	#moving down
	if movement[1] > 0:
		if (player_rect.bottom < background.get_height()):
			if (background.get_height() - player_rect.bottom < speed):
				player_move[1] = background.get_height() - player_rect.bottom
				on_ground = True

			#else:
				#player_move[1] = speed
		#move the viewport		
		if (player_rect.bottom > view_rect.bottom - scroll_buff and view_rect.bottom < background.get_height()):
			if (background.get_height() - view_rect.bottom < player_move[1]):
				view_move[1] = background.get_height() - view_rect.bottom
			else:
				view_move[1] = player_move[1]
						
	#update viewport and player and return.
	view_rect = view_rect.move(view_move)
	player_rect = player_rect.move(player_move)
	

"""
"""	
def collision_detect(ent_rect, ent_move):
	
	ent_left = (ent_rect.left // tilesize) 
	ent_right = math.ceil(ent_rect.right / tilesize)
	ent_top = (ent_rect.top // tilesize)
	ent_bottom = math.ceil(ent_rect.bottom / tilesize)
	diff = 0
	
	#Left side collision
	if ent_move[0] < 0:
		for i in range(1 if ent_rect.top % tilesize == 0 else 2):
			if (map.map[(ent_rect.left + ent_move[0]) // tilesize] [ent_top + i] [1] == False):
				diff = (ent_left * tilesize) - ent_rect.left
				if (ent_move[0] < diff): ent_move[0] = diff
				
	#Right side collision
	if ent_move[0] > 0:
		for i in range(1 if ent_rect.top % tilesize == 0 else 2):
			if (map.map[(ent_rect.right + ent_move[0] -1) // tilesize] [ent_top + i] [1] == False):
				diff = (ent_right * tilesize) - ent_rect.right
				if (ent_move[0] > diff): ent_move[0] = diff
				
	#Top side collision
	if ent_move[1] < 0:
		for i in range(1 if ent_rect.left % tilesize == 0 else 2):
			if (map.map[ent_left + i] [(ent_rect.top + ent_move[1]) // tilesize] [1] == False):
				diff = (ent_top * tilesize) - ent_rect.top
				if (ent_move[1] < diff): ent_move[1] = diff
				
	#Bottom side collision
	if ent_move[1] > 0:
		for i in range(1 if ent_rect.left % tilesize == 0 else 2):
			if (map.map[ent_left + i] [(ent_rect.bottom + ent_move[1] -1) // tilesize] [1] == False):
				diff = (ent_bottom * tilesize) - ent_rect.bottom
				if (ent_move[1] > diff): ent_move[1] = diff
	
	return ent_move
			
	
"""
"""
if __name__ == '__main__':

	for x in range(map.mapWidth):
		for y in range(map.mapHeight):
			tile = map.map[x][y][0]
			background.blit(tile, (x*tilesize, y*tilesize))
			
	#bgx2 = pygame.Surface((map.drawWidth*2, map.drawHeight*2))
	#pygame.transform.scale2x(background, bgx2)
	
	#THE ALMIGHTY GAME LOOP
	while 1:		
		event_update()
		movement_update()

		#print("Resize width: ", window_sized.width)
		#print("Resize height: ", window_sized.height)

		#w_ratio = window_sized.width // window_rect.width
		#h_ratio = window_sized.height // window_rect.height
		
		#bg_new_dim = (w_ratio*background.get_width(), h_ratio*background.get_height())
		
		#bg_new = pygame.Surface(bg_new_dim)
		#pygame.transform.scale(background, (bg_new_dim), bg_new)
		
		screen.fill(black)				
		viewport = background.subsurface(view_rect)
		screen.blit(viewport, window_rect)
		#screen.blit(player, player_rect)
		screen.blit(player, pygame.Rect(player_rect.left - view_rect.left, player_rect.top - view_rect.top, tilesize, tilesize))
		pygame.display.flip() 
		
		clock.tick(80)
				
