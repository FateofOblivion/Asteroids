# this allows us to use code from
# the open-source pygame library
# throughout this file
from constants import *
import pygame
def main():
    pygame.init()
    pygame.time.Clock.tick()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen,(0,0,0))
        pygame.display.flip()
        pygame.time.Clock.tick(60)
        dt = pygame.time.Clock.tick(60) / 1000
    

if __name__ == "__main__":
    main()
