'''
Created on Jun 3, 2014

@author: Scurvy
'''

import pygame, sys
from pygame.locals import *

tilesize = 32 #size of the square tile 
windowWidth = 640
windowHeight = 480
speed = [2, 2]
speed2 = [1,1]

pygame.init()
	
#Create the window
screen = pygame.display.set_mode((windowWidth, windowHeight))

#Load the image
tile = pygame.image.load("rect_gray0.png")
tilerect = tile.get_rect()#(0, 0, tilesize, tilesize)
tile2rect = tile.get_rect()

while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
			
	tilerect = tilerect.move(speed)
	if tilerect.left < 0 or tilerect.right > windowWidth:
		speed[0] = -speed[0]
	if tilerect.top < 0 or tilerect.bottom > windowHeight:
		speed[1] = -speed[1]
		
	tile2rect = tile2rect.move(speed2)
	if tile2rect.left < 0 or tile2rect.right > windowWidth:
		speed2[0] = -speed2[0]
	if tile2rect.top < 0 or tile2rect.bottom > windowHeight:
		speed2[1] = -speed2[1]
            
	screen.fill((0, 0, 0))
	screen.blit(tile, tilerect) #Should be top-left corner?
	screen.blit(tile, tile2rect)
	pygame.display.flip()