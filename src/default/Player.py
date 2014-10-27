'''
Created on Oct 25, 2014

@author: Rex Baumeister
'''

import os, sys, math
import pygame
from pygame.locals import *
import Entity

class Player from Entity:
	
	def __init__(self):
		
	"""
	"""
	def movement_update(self):
		global player_rect
		global view_rect
		global scroll_buff
		global ground_speed
		global jump_speed
		global on_ground
		global player_move
		global frame_number
		global time_grounded
		
		view_move = [0,0]
		movement = [0,0]
		speed_value = ground_speed if on_ground else air_speed
		
		#determine if there is movement
		movement[0] = keys[1] - keys[0]
		
		if on_ground == True: 
			time_grounded += 1
			player_move[0] = movement[0] * ground_speed
			if keys[2] == 1 and keys[3] == 0 and time_grounded >= jump_delay:
				player_move[1] = -jump_speed
				movement[1] = -1
				
			else: # if on the ground, player should try to move down
				player_move[1] = 1 
				movement[1] = 1
		
		else: #if in the air, accelerate down.
			movement[1] = player_move[1] #Only the charge of movement matters, not the voltage.
			time_grounded = 0 
			player_move[0] = movement[0] * air_speed
			if frame_number % fall_inertia == 0:
				player_move[1] += 1 #accelerate towards ground at rate of 1/6th of a pixel per frame^2
						
		player_move = collision_detect(player_rect, player_move)
	
		#moving left
		if movement[0] < 0:
			if (player_rect.left > 0):
				if (player_rect.left < -player_move[0]):
					player_move[0] = -player_rect.left
				
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
	
			#move the viewport		
			if (player_rect.top < view_rect.top + scroll_buff and view_rect.top > 0):
				if (view_rect.top < -player_move[1]):
					view_move[1] = -view_rect.top
				else:
					view_move[1] = player_move[1]
			
		#moving down
		if movement[1] > 0:
			if (player_rect.bottom < background.get_height()):
				if (background.get_height() - player_rect.bottom < speed_value):
					player_move[1] = background.get_height() - player_rect.bottom
					
			#move the viewport		
			if (player_rect.bottom > view_rect.bottom - scroll_buff and view_rect.bottom < background.get_height()):
				if (background.get_height() - view_rect.bottom < player_move[1]):
					view_move[1] = background.get_height() - view_rect.bottom
				else:
					view_move[1] = player_move[1]
					
		if player_move[1] == 0:
			on_ground = True
		else:
			on_ground = False
							
		#update viewport and player and return.
		view_rect = view_rect.move(view_move)
		player_rect = player_rect.move(player_move)