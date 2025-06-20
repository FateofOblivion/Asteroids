import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def collisions(self, shape2):
        return self.position.distance_to(shape2.position) <= self.radius + shape2.radius
    
    def draw(self, Screen):
        pygame.draw.polygon(Screen,(225,225,225),self.triangle(),2)
        

    def update(self, dt):
        # sub-classes must override
        pass
