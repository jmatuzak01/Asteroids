import random
import pygame
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen, color="white"):
        pygame.draw.circle(screen, color, self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        # we want to create two new asteroids with the same position and smaller radius, but different velocities
        new_asteroid_vector1 = self.velocity.rotate(random.uniform(20,50))
        new_asteroid_vector2 = self.velocity.rotate(random.uniform(-20,-50))
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        #make new asteroids with the same position and smaller radius, but different velocities
        new_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid1.velocity = new_asteroid_vector1 * 1.2
        new_asteroid2.velocity = new_asteroid_vector2 * 1.2

        
