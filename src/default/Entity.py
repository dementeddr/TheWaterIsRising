'''
Created on Oct 25, 2014

@author: Rex Baumeister
'''
import os, sys, math
import pygame
from pygame.locals import *

class Entitiy:
	
	
	def __init__(self):
		self.rect = pygame.Rect()
		self.sprite = pygame.image()

	def movement_update(self):
			