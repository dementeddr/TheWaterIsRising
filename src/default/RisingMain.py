'''
Created on May 10, 2014

@author: Scurvy
'''

import pygame, sys
from pygame.locals import *

pygame.init()
print("Initializing")

windowWidth = 640
windowHeight = 480
windowSize = windowWidth, windowHeight

speed = [1, 1] #Array/List declaration
black = (0,0,0) #Tuple declaration

screen = pygame.display.set_mode(windowSize)

axe = pygame.image.load("battle_axe2.png")
axeRect = axe.get_rect()

while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
			
	axeRect = axeRect.move(speed)
	if axeRect.left < 0 or axeRect.right > windowWidth:
		speed[0] = -speed[0]
	if axeRect.top < 0 or axeRect.bottom > windowHeight:
		speed[1] = -speed[1]
		
	screen.fill(black)
	screen.blit(axe, axeRect)
	pygame.display.flip()

