#
# pygame_test.py
# Practicing with pygame
# Last Modified: 8/16/2017
# Modified By: Andrew Roberts
#

from collections import namedtuple
import pygame
import math
pygame.init()

DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600

Color = namedtuple("Color", ["red", "green", "blue"])
black = Color(0, 0, 0)
white = Color(255, 255, 255)
light_blue = Color(153, 204, 255)

mr_pb_png = pygame.image.load("game_character.png")
MR_PB_VELOCITY = 10

def mr_pb(x, y):
	game_display.blit(mr_pb_png, (x, y))
x = DISPLAY_WIDTH * .48
y = DISPLAY_HEIGHT * .87

game_display = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption("Practice Game")
clock = pygame.time.Clock()

lost = False
x_change = 0 

while not lost: 
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			lost = True		
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				x_change = -MR_PB_VELOCITY
			if event.key == pygame.K_RIGHT:
				x_change = MR_PB_VELOCITY
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
				x_change = 0	
	x += x_change

	game_display.fill(light_blue)	
	mr_pb(x, y)
	pygame.display.update()
	clock.tick(60)

pygame.quit()

