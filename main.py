from constants import *
from player import Player
import pygame
from asteroidfield import AsteroidField
from asteroid import Asteroid
def main():
    print("Starting Asteroids")
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    #Create Groups
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    #Set containers
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = updateable
    asteroid_field = AsteroidField()
    #Setup Display 
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updateable, drawable)
    Player.containers = (updateable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)  # ✅ Create player object here
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        updateable.update(dt)
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
