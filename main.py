import pygame
from constants import *
from player import *
from circleshape import *
from asteroidfield import *
from asteroid import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    x = SCREEN_WIDTH/2
    y = SCREEN_HEIGHT/2
    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable,drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()
  
    subject = Player(x,y)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        for ob in drawable:
            ob.draw(screen)
        updatable.update(dt)
        pygame.display.flip()
        dt = clock.tick(60)/1000  



if __name__ == "__main__":
    main()
