'''
Created on Jun 3, 2014

@author: Scurvy
'''

import sys

flip = []

for x in range(6):
	flip.append([])
	for y in range(4):
		flip[x].append(x + y)
		
print(flip)