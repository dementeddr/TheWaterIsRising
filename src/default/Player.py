'''
Created on Oct 25, 2014

@author: Rex Baumeister
'''

import os, sys, math
import pygame
from pygame.locals import *
import Entity

class Player(Entity.Entity):
	
	def __init__(self, world):
		super(Entity.Entity, self).__init__()
		
		self.view_rect = world.window_rect.copy() #defines the viewport
		self.scroll_buff = world.tilesize * 5	#How close the player can get to an edge before the camera moves
	
		self.sprite = pygame.image.load("human_m.png").convert()
		self.ent_rect = pygame.Rect(200, 100, world.tilesize, world.tilesize) #Starting location
		
		#All of this SHOULD NOT BE NECESSARY. Grah, this hurts so much.
		self.on_ground = False
		self.ground_speed = 3
		self.air_speed = 2		#Defines speed of side-to-side movement in air
		self.jump_speed = 8	#Defines how far up the entity can jump
		self.jump_delay = 8	#The number of frames after landing before you can jump again.
		self.fall_inertia = 8	#Defines how fast the entity falls in air
		self.time_grounded = 0	#Number of frames since landing
		self.ent_move = [0,0] #This has to be saved so that parabolic falling will work 


	
	"""
	"""
	def movement_update(self, world):
		
		#These exist soley to make this code easier to read.
		ground_speed = self.ground_speed
		air_speed = self.air_speed
		jump_speed = self.jump_speed
		jump_delay = self.jump_delay
		fall_inertia = self.fall_inertia
		
		#These get assigned back to their self. versions at the end.
		ent_rect = self.ent_rect
		ent_move = self.ent_move
		view_rect = self.view_rect
				
		view_move = [0,0]
		movement = [0,0]
		speed_value = ground_speed if self.on_ground else air_speed
		
		#determine if there is side-to-side movement
		movement[0] = world.keys[1] - world.keys[0]
		
		if self.on_ground == True: 
			self.time_grounded += 1
			ent_move[0] = movement[0] * ground_speed #
			if world.keys[2] == 1 and world.keys[3] == 0 and self.time_grounded >= jump_delay:
				ent_move[1] = -jump_speed
				movement[1] = -1
				
			else: # if on the ground, player should try to move down
				ent_move[1] = 1 
				movement[1] = 1
		
		else: #if in the air, accelerate down.
			movement[1] = ent_move[1] #Only the charge of movement matters, not the voltage.
			time_grounded = 0 
			ent_move[0] = movement[0] * air_speed
			if world.frame_number % fall_inertia == 0:
				ent_move[1] += 1 #accelerate towards ground at rate of 1/6th of a pixel per frame^2
						
		ent_move = self.collision_detect(world)
	
		#moving left
		if movement[0] < 0:
			if (ent_rect.left > 0):
				if (ent_rect.left < -ent_move[0]):
					ent_move[0] = -ent_rect.left
				
			#move the viewport		
			if (ent_rect.left < view_rect.left + self.scroll_buff and view_rect.left > 0):
				if (view_rect.left < -ent_move[0]):
					view_move[0] = -view_rect.left
				else:
					view_move[0] = ent_move[0]
			
		#moving right
		if movement[0] > 0:
			if (ent_rect.right < world.background.get_width()):
				if (world.background.get_width() - ent_rect.right < ent_move[0]):
					ent_move[0] = world.background.get_width() - ent_rect.right
				
			#move the viewport		
			if (ent_rect.right > view_rect.right - self.scroll_buff and view_rect.right < world.background.get_width()):
				if (world.background.get_width() - view_rect.right < ent_move[0]):
					view_move[0] = world.background.get_width() - view_rect.right
				else:
					view_move[0] = ent_move[0]
					
		#moving up
		if movement[1] < 0:
			if (ent_rect.top > 0):
				if (ent_rect.top < ent_move[1]):
					ent_move[1] = -ent_rect.top
	
			#move the viewport		
			if (ent_rect.top < view_rect.top + self.scroll_buff and view_rect.top > 0):
				if (view_rect.top < -ent_move[1]):
					view_move[1] = -view_rect.top
				else:
					view_move[1] = ent_move[1]
			
		#moving down
		if movement[1] > 0:
			if (ent_rect.bottom < world.background.get_height()):
				if (world.background.get_height() - ent_rect.bottom < speed_value):
					ent_move[1] = world.background.get_height() - ent_rect.bottom
					
			#move the viewport		
			if (ent_rect.bottom > view_rect.bottom - self.scroll_buff and view_rect.bottom < world.background.get_height()):
				if (world.background.get_height() - view_rect.bottom < ent_move[1]):
					view_move[1] = world.background.get_height() - view_rect.bottom
				else:
					view_move[1] = ent_move[1]
					
		if ent_move[1] == 0:
			self.on_ground = True
		else:
			self.on_ground = False
							
		#update viewport and player and return.
		view_rect = view_rect.move(view_move)
		ent_rect = ent_rect.move(ent_move)
		
		self.ent_rect = ent_rect
		self.ent_move = ent_move
		self.view_rect = view_rect
		