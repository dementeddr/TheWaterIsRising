'''
Created on Jun 11, 2014

@author: Scurvy
'''

import os, sys
import pygame
from pygame.locals import *

"""
"""
class TileMap1:
	
	map = []
	mapWidth = 0
	mapHeight = 0
	drawWidth = 0
	drawHeight = 0
	
	"""
	"""
	def __init__(self, tilesize, mapWidth, mapHeight):
		self.mapWidth = mapWidth
		self.mapHeight = mapHeight
		
		self.drawWidth = mapWidth * tilesize
		self.drawHeight = mapHeight * tilesize

		floor1 = pygame.image.load("rect_gray0.png").convert()
		floor2 = pygame.image.load("floor_vines0.png").convert()
				
		for x in range(mapWidth):
			line = []
			self.map.append(line)
			for y in range(mapHeight):
				if y == 0 or y == mapHeight-1 or x == 0 or x == mapWidth-1:
					line.append(floor2.subsurface((0,0,tilesize,tilesize)))
				else:
					line.append(floor1.subsurface((0,0,tilesize,tilesize)))
					
		return