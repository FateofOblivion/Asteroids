# this allows us to use code from
# the open-source pygame library
# throughout this file
from constants import *
import pygame
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock.tick()
    dt = 0
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen,(0,0,0))
        pygame.display.flip()
        pygame.time.Clock.tick(60)
        dt = clock.tick(60) / 1000
    

if __name__ == "__main__":
    main()
