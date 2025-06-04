import pygame
import random

from circleshape import *
from constants import *

class Asteroid(CircleShape):
    
    def __init__ (self, x, y, radius):
        super().__init__(x,y,radius)

    def draw(self, screen):
        pygame.draw.circle(screen,"white",self.position,self.radius,width = 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else :
            random_angle = random.uniform(20,50)
            split1 = pygame.math.Vector2.rotate(self.velocity,random_angle)
            split2 = pygame.math.Vector2.rotate(self.velocity,-random_angle)

            new_radius = self.radius - ASTEROID_MIN_RADIUS
            
            asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
            
            asteroid1.velocity = split1 * 1.3
            asteroid2.velocity = split2 * 1.2

