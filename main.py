import sys,os
import pygame
from constants import SCREEN_HEIGHT,SCREEN_WIDTH,PLAYER_RADIUS
from logger import log_event, log_state
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from logger import log_state
from shot import Shot

def main():
    pygame.init()
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}, Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    gameClock = pygame.time.Clock()
    dt: int = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    AsteroidField.containers = updatable
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    Shot.containers = (updatable, drawable, shots)
    playerIcon = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)
    asteroid_field = AsteroidField()

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Quitting game.")
                pygame.quit()
                return
        screen.fill("black")
        for sprite in drawable: # draw all sprites
            sprite.draw(screen)
        updatable.update(dt) # update all sprites
        
        for asteroid in asteroids: # check for collisions with player
            if asteroid.collides_with(playerIcon):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
                return
        
        for asteroid in asteroids: # check for collisions with shots
            for shot in shots:
                if asteroid.collides_with(shot):
                    log_event("asteroid_shot")
                    shot.kill()
                    asteroid.split()

        # asteroid–asteroid collisions
        asteroid_list = list(asteroids)
        for i in range(len(asteroid_list)):
            for j in range(i + 1, len(asteroid_list)):
                a = asteroid_list[i]
                b = asteroid_list[j]

                if a.collides_with(b):
                    a.resolve_collision(b) #bounce asteroid a off of asteroid b
        
        
        pygame.display.flip()

        dt = gameClock.tick(60) / 1000  # Limit to 60 FPS and convert to seconds


if __name__ == "__main__":
    main()
