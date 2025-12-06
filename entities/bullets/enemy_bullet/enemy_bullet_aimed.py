import pygame
import math

class EnemyBulletAimed(pygame.sprite.Sprite):
    def __init__(self, x, y, target_pos, speed=200):
        super().__init__()
        self.image = pygame.Surface((8, 8), pygame.SRCALPHA)
        pygame.draw.circle(self.image, (255, 0, 0), (4, 4), 4)
        self.rect = self.image.get_rect(center=(x, y))
        self.mask = pygame.mask.from_surface(self.image)

        dx = target_pos[0] - x
        dy = target_pos[1] - y
        dist = max(1, math.hypot(dx, dy))
        self.velocity = pygame.math.Vector2(dx / dist, dy / dist)

        self.speed = speed
        self.pos = pygame.math.Vector2(self.rect.center)

    def update(self, dt):
        self.pos += self.velocity * (self.speed * dt / 1000)
        self.rect.center = (int(self.pos.x), int(self.pos.y))

        if (self.rect.top > 600 or self.rect.bottom < 0 or 
            self.rect.right < 0 or self.rect.left > 1000):
            self.kill()