import pygame
from constants import SCREEN_HEIGHT,SCREEN_WIDTH,PLAYER_RADIUS
from logger import log_state
from player import Player

def main():
    pygame.init()
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}, Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    gameClock = pygame.time.Clock()
    dt: int = 0
    playerIcon = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Quitting game.")
                pygame.quit()
                return
        screen.fill("black")
        playerIcon.draw(screen)
        playerIcon.update(dt)
        pygame.display.flip()
        dt = gameClock.tick(60) / 1000  # Limit to 60 FPS and convert to seconds


if __name__ == "__main__":
    main()
