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

pygame.init()
	
#Create the window
screen = pygame.display.set_mode((windowWidth, windowHeight))
screen.fill((0,0,0))

#Load the image
tile = pygame.image.load("rect_gray0.png")
rect = tile.get_rect()#(0, 0, tilesize, tilesize)
sub = tile.subsurface(rect)
image = pygame.Surface((tilesize, tilesize))

rect = rect.move(speed)

while pygame.event.wait().type != pygame.locals.QUIT:
	image.blit(tile, rect) #Should be top-left corner?
	pygame.display.flip()