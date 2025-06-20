# this allows us to use code from
# the open-source pygame library
# throughout this file
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
import pygame
import sys
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updateable,drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable,)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidField = AsteroidField()
 
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        

        
        updateable.update(dt)
        for asteroids in asteroidField:
            if asteroids.collisions(player):
                print("Game over!")
                sys.exit()
        pygame.Surface.fill(screen,(0,0,0))
        for drawable_object in drawable:
            drawable_object.draw(screen)
        pygame.display.flip()
        
        dt = clock.tick(60) / 1000
    

if __name__ == "__main__":
    main()
