import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import *
from circleshape import CircleShape

clock = pygame.time.Clock()
dt = 0

def main():
    pygame.init()
    
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        delta_ms = clock.tick(60)
        dt = delta_ms / 1000
        screen.fill("black")
        for sprite in drawable:
            sprite.draw(screen)
        updatable.update(dt)
        player.shot_timer -= dt
        for asteroid in asteroids:
            if player.check_for_collisions(asteroid):
                print("Game over!")
                sys.exit()
        for shot in player.shots:
            for asteroid in asteroids:
                if shot.check_for_collisions(asteroid):
                    asteroid.split()
                    shot.kill()
            shot.update(dt)
            shot.draw(screen) 
        player.shots = [shot for shot in player.shots if shot.alive]
        pygame.display.flip()

if __name__ == "__main__":
    main()
