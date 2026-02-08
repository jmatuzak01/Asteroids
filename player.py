import pygame
from constants import *
from circleshape import CircleShape
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y, PLAYER_RADIUS, shot_cooldown = 0.0):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shot_cooldown = shot_cooldown

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH)

    def update(self,dt):
        self.shot_cooldown -= dt # reduce cooldown timer by the time since last frame
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]: # rotate left
            self.rotate(-dt)
        if keys[pygame.K_d]: # rotate right
            self.rotate(dt)
        if keys[pygame.K_w]: # move forward
            self.move(dt)
        if keys[pygame.K_s]: # move backward
            self.move(-dt)
        if keys[pygame.K_SPACE]: # shoot
            if self.shot_cooldown > 0:
                return
            self.shot_cooldown = PLAYER_SHOOT_COOLDOWN_SECONDS
            new_shot = self.shoot()
            new_shot.add(Shot.containers)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
    
    def move(self, dt):
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed = rotated_vector * PLAYER_SPEED * dt
        self.position += rotated_with_speed

        min_x = self.radius
        max_x = SCREEN_WIDTH - self.radius
        min_y = self.radius
        max_y = SCREEN_HEIGHT - self.radius

        self.position.x = max(min_x, min(max_x, self.position.x))
        self.position.y = max(min_y, min(max_y, self.position.y))

    def shoot(self):
        new_shot = Shot(self.position.x, self.position.y, pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED)
        return new_shot
    