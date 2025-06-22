import pygame
import random
from constants import *
from circleshape import CircleShape
class Asteroid(CircleShape):
	def __init__(self,x,y,radius):
		super().__init__(x, y, radius)
		for group in Asteroid.containers:
			group.add(self)
	
	def draw(self,screen):
		pygame.draw.circle(screen,(255,255,255),tuple(self.position),self.radius, 2)
	def split(self):
		self.kill()
		if self.radius <= ASTEROID_MIN_RADIUS:
			return
		else:
			random_angle = random.uniform(20,50)
			new_vector1 = (self.velocity.rotate(random_angle)) * 1.2
			new_vector2 = (self.velocity.rotate(-random_angle)) * 1.2
			new_radius = self.radius - ASTEROID_MIN_RADIUS
			new_asteriod_1 = Asteroid(self.position.x,self.position.y,new_radius)
			new_asteriod_2 = Asteroid(self.position.x,self.position.y,new_radius)
			new_asteriod_1.velocity = new_vector1
			new_asteriod_2.velocity = new_vector2
			
	def update(self,dt):
		self.position += (self.velocity * dt)