'''
Created on Dec 22, 2014

@author: Scurvy
'''
import pygame
from TileMap1 import *
from TileMap2 import *
from pygame.locals import *

class World(object):

	def __init__(self, win_size):
		self.window_size  = win_size	#Size of game window. Resizing is an eventual goal.
		self.tilesize = 32 	#Pixel size of the tiles in this tile-based game
		self.keys = [0,0,0,0] 	#Left, Right, Up, Down
		self.frame_number = 0	#number of frames since start of game. 
								#This will need to handle arbitrary size at some point.

		self.map = TileMap1(self.tilesize, 30, 24)	#Tilemap of the current room. Right now the game only has
					#two rooms and you have to hard-code which one you want.
					#This is temporary while physics are getting fleshed out.
			
		self.background = pygame.Surface((self.map.mapWidth * self.tilesize, self.map.mapHeight * self.tilesize))
		self.window_rect = pygame.Rect(0, 0, self.window_size[0], self.window_size[1])
