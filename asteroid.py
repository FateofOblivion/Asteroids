import pygame
from constants import *
from circleshape import CircleShape
class Asteroid(CircleShape):
	def __init__(self,x,y,radius):
		super().__init__(x, y, radius)
		for group in Asteroid.containers:
			group.add(self)
	
	def draw(self,screen):
		pygame.draw.circle(screen,(0,0,0),tuple(self.position),self.radius, 2)
	
	def update(self,dt):
		self.position += (self.velocity * dt)