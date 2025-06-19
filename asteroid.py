import pygame
from constants import *
from circleshape import CircleShape
class Asteroid(CircleShape):
	def __init__(self,x,y,radius):
		self.x = x
		self.y = y
		self.radius = radius
		for group in Asteroid.containers:
			group.add(self)
	
	def draw(self):
		pygame.draw.cirlce((self.x ,self.y),self.radius, 2)
	
	def update(self):
		self.position += (self.velocity * dt)