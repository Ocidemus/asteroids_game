import pygame
from player import *

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

    def draw(self, screen):
        pass

    def update(self, dt):
        # sub-classes must override
        pass
    
    def collision(self, othershape):
        distance = pygame.math.Vector2.distance_to(self.position,othershape.position)
        if distance > (self.radius + othershape.radius):
            return False
        else:
            return True


