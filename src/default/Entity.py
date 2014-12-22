'''
Created on Oct 25, 2014

@author: Rex Baumeister
'''
import os, sys, math
import pygame
from pygame.locals import *

class Entitiy(object):
	
	ent_rect = pygame.Rect()
	sprite = pygame.image()
	ground_speed = 3
	air_speed = 2	#Defines speed of side-to-side movement in air
	jump_speed = 8	#Defines how far up the entity can jump
	on_ground
	time_grounded	#Number of frames since landing
	jump_delay = 8	#The number of frames after landing before you can jump again.
	fall_inertia = 8#Defines how fast the entity falls in air
	ent_move 	#vector of 
	
	def __init__(self):
		global ent_rect
		global sprite
		global on_ground
		global ground_speed
		global air_speed
		global jump_speed
		global jump_delay
		global fall_inertia
		global time_grounded
		global ent_move
		
		on_ground = False

	def movement_update(self):
		print('something') #placeholder
		
		
		
	def collision_detect(self, world):
		
		ent_left = (ent_rect.left // world.tilesize) 
		ent_right = math.ceil(ent_rect.right / world.tilesize)
		ent_top = (ent_rect.top // world.tilesize)
		ent_bottom = math.ceil(ent_rect.bottom / world.tilesize)
		diff = 0
		
		#Left side collision
		if ent_move[0] < 0:
			for i in range(1 if ent_rect.top % world.tilesize == 0 else 2):
				if (map.map[(ent_rect.left + ent_move[0]) // world.tilesize] [ent_top + i] [1] == False):
					diff = (ent_left * world.tilesize) - ent_rect.left
					if (ent_move[0] < diff): ent_move[0] = diff
					
		#Right side collision
		if ent_move[0] > 0:
			for i in range(1 if ent_rect.top % world.tilesize == 0 else 2):
				if (map.map[(ent_rect.right + ent_move[0] -1) // world.tilesize] [ent_top + i] [1] == False):
					diff = (ent_right * world.tilesize) - ent_rect.right
					if (ent_move[0] > diff): ent_move[0] = diff
					
		#Top side collision
		if ent_move[1] < 0:
			for i in range(1 if ent_rect.left % world.tilesize == 0 else 2):
				if (map.map[ent_left + i] [(ent_rect.top + ent_move[1]) // world.tilesize] [1] == False):
					diff = (ent_top * world.tilesize) - ent_rect.top
					if (ent_move[1] < diff): ent_move[1] = diff
					
		#Bottom side collision
		if ent_move[1] > 0:
			for i in range(1 if ent_rect.left % world.tilesize == 0 else 2):
				if (map.map[ent_left + i] [(ent_rect.bottom + ent_move[1] -1) // world.tilesize] [1] == False):
					diff = (ent_bottom * world.tilesize) - ent_rect.bottom
					if (ent_move[1] >= diff): 
						ent_move[1] = diff
		
		return ent_move
				