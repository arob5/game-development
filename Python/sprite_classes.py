#
# sprite_classes.py
# Clases for Mr. PB and ball
# Last Modified: 8/17/2017
# Modified By: Andrew Roberts
#

import pygame

class Vector():
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __add__(self, vec):
		try: 
			return Vector(self.x + vec.x, self.y + vec.y)
		except TypeError:
			print("Argument must be a vector")
	
	def return_coordinates_tuple(self):
		return (self.x, self.y)

class MrPB():
	def __init__(self, game_display, image, speed, x, y):
		self.sprite = pygame.image.load(image)	
		self.speed = speed
		self.vel = Vector(0, 0)
		self.pos = Vector(x, y)
		self.game_display = game_display
 
	def draw(self):
		self.pos = self.pos + self.vel
		self.check_boundaries()
		self.game_display.blit(self.sprite, self.pos.return_coordinates_tuple())

	def check_boundaries(self):
		w, h = self.game_display.get_size() 
		x, y = self.pos.return_coordinates_tuple()

		if x > w:
			self.pos = Vector(0, y)
		if x < 0:
			self.pos = Vector(w, y)
	
	def move_mr_pb(self, event):	
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				self.vel = Vector(-self.speed, 0) 
			if event.key == pygame.K_RIGHT:
				self.vel = Vector(self.speed, 0)

		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
				self.vel = Vector(0, 0)	
