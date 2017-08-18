#
# sprite_classes.py
# Clases defining a vector, the main character for the game, and the obstacles (balls)
# Last Modified: 8/17/2017
# Modified By: Andrew Roberts
#

import numpy as np
import pygame
import math

class Vector():
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __add__(self, vec):
		try: 
			return Vector(self.x + vec.x, self.y + vec.y)
		except TypeError:
			print("Argument must be a vector")

	def __mul__(self, scalar):
		try:
			return Vector(self.x * scalar, self.y * scalar)
		except TypError:
			print("Scalar value must be int or float")

	__rmul__ = __mul__
		
	def length(self):
		return math.sqrt(self.x*self.x + self.y*self.y) 

	def normalize(self):
		return self * (1 / self.length())
	
	def return_coordinates_tuple(self):
		return (self.x, self.y)

class MrPB():
	def __init__(self, game_display, image, speed, x, y, floor):
		self.sprite = pygame.image.load(image)	
		self.speed = speed
		self.vel = Vector(0, 0)
		self.grav = Vector(0, 6)
		self.pos = Vector(x, y)
		self.mass = 3
		self.game_display = game_display
		self.sprite_size = (27, 80)
		self.floor = floor
 
	def draw(self):
		jumping = self.pos.y < self.floor
		
		if jumping:
			if self.vel.y < 0: 
				y_update = -(.5 * self.mass * (self.vel.y * self.vel.y)) 
			else: 
				y_update = .5 * self.mass * (self.vel.y * self.vel.y)
			self.pos = Vector(self.pos.x + self.vel.x, self.pos.y + y_update)
			self.vel = Vector(self.vel.x, self.vel.y + .5)
		else:
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
		if y > self.floor:
			self.pos = Vector(self.pos.x, self.floor)
	
	def update_mr_pb(self, event):	
		if self.pos.y == self.floor:
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					self.vel = Vector(-self.speed, 0) 
				if event.key == pygame.K_RIGHT:
					self.vel = Vector(self.speed, 0)
				if event.key == pygame.K_UP:
					self.vel = Vector(self.vel.x, -6)
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
					self.vel = Vector(0, 0)	

class Ball():
	def __init__(self, surface, pos, speed_scale=4, color=(255, 153, 102)):
		self.surface = surface
		x, y = pos
		self.pos = Vector(x, y)
		self.speed = speed_scale
		self.radius = np.random.randint(low=4, high=30)
		self.vel = speed_scale * self.random_direction()  
		self.color = color
	
	def random_direction(self):
		x = np.random.randint(low=-20, high=20)
		y = np.random.randint(low=-20, high=20)

		v = Vector(x, y).normalize()
		v.x = int(np.round(v.x)) + np.random.randint(low=-2, high=2)
		v.y = int(np.round(v.y)) + np.random.randint(low=-2, high=2)

		if v.x == 0:
			v.x += np.random.randint(low=-2, high=2)
		if v.y == 0:
			v.y += np.random.randint(low=-2, high=2)

		return v

	def check_boundaries(self):
		x, y = self.pos.return_coordinates_tuple()
		w, h = self.surface.get_size()

		if ((y+self.radius) >= h) or ((y-self.radius) <= 0):
			self.vel.y *= -1
		if ((x+self.radius) >= w) or ((x-self.radius) <= 0):
			self.vel.x *= -1
			
	def draw(self):
		self.pos = self.pos + self.vel
		self.check_boundaries()	
		pygame.draw.circle(self.surface, self.color, self.pos.return_coordinates_tuple(), self.radius)

	def detect_collision(self, mr_pb):
		x1, y1 = mr_pb.pos.return_coordinates_tuple()
		w, h = mr_pb.sprite_size
		x2, y2 = self.pos.return_coordinates_tuple()
		r = self.radius

		return (x1+w >= x2-r) and (y1 <= y2+r) and (x1 <= x2+r) and (y1+h >= y2-r)
	

