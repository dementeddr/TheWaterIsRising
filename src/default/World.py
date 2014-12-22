'''
Created on Dec 22, 2014

@author: Scurvy
'''
import pygame
from TileMap1 import *
from TileMap2 import *
from pygame.locals import *

class World(object):

	windowSize = (640, 480)
	tilesize = 32
	keys = [0,0,0,0] #Left, Right, Up, Down
	background = pygame.Surface((map.mapWidth*tilesize, map.mapHeight*tilesize))
	frame_number = 0
	map = TileMap1(tilesize, 30, 24) #Load the tile map. 

	def __init__(self):
		global windowSize	#Size of game window. Resizing is an eventual goal.
		global tilesize #Pixel size of the tiles in this tile-based game
		global keys		#Holds if arrow keys are pressed or not.
		global frame_number #number of frames since start of game. 
							#This will need to handle arbitrary size at some point.
		global background
		global map	#Tilemap of the current room. Right now the game only has
					#two rooms and you have to hard-code which one you want.
					#This is temporary while physics are getting fleshed out.
		
		