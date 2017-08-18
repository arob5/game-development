#
# pygame_test.py
# Practicing with pygame
# Last Modified: 8/17/2017
# Modified By: Andrew Roberts
#

from collections import namedtuple
import sprite_classes
import pygame
import math
pygame.init()

DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600

Color = namedtuple("Color", ["red", "green", "blue"])
black = Color(0, 0, 0)
white = Color(255, 255, 255)
light_blue = Color(153, 204, 255)

game_display = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption("Practice Game")
clock = pygame.time.Clock()

# Character sprite
MR_PB_VELOCITY = 10
mr_pb_x = DISPLAY_WIDTH * .48
mr_pb_y = DISPLAY_HEIGHT * .87
mr_pb = sprite_classes.MrPB(game_display, "game_character.png", MR_PB_VELOCITY, mr_pb_x, mr_pb_y, mr_pb_y)

# Character obstacles
ball_array = [sprite_classes.Ball(game_display, (400, 300)) for i in range(10)]

def game_loop():
	game_exit = False

	while not game_exit: 
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				game_exit = True		
			mr_pb.update_mr_pb(event)

		game_display.fill(light_blue)	

		mr_pb.draw()
		for ball in ball_array:
			ball.draw()

		pygame.display.update()
		clock.tick(60)
game_loop()
pygame.quit()

