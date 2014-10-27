'''
Created on Oct 25, 2014

@author: Rex Baumeister
'''
import os, sys, math
import pygame
from pygame.locals import *

class Entitiy(object):
	
	
	def __init__(self):
		self.rect = pygame.Rect()
		self.sprite = pygame.image()
		
		self.on_ground = False
		self.ground_speed = 3
		self.air_speed = 2
		self.jump_speed = 8
		self.jump_delay = 3
		self.fall_inertia = 6

	def movement_update(self):
			