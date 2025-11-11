import pygame
import math

class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos, speed=-500):
        super().__init__()
        self.image = pygame.Surface((8, 8), pygame.SRCALPHA)
        pygame.draw.circle(self.image, (255, 0, 0), (4, 4), 4)
        self.rect = self.image.get_rect(center=pos)
        self.mask = pygame.mask.from_surface(self.image)
        self.speed = speed

    def update(self, dt):
        self.rect.y += self.speed * (dt / 1000)
        if self.rect.bottom < 0:
            self.kill()

class EnemyBullet(pygame.sprite.Sprite):
    def __init__(self, x, y, target_pos, speed=250):
        super().__init__()
        self.image = pygame.Surface((8, 8), pygame.SRCALPHA)
        pygame.draw.circle(self.image, (255, 0, 0), (4, 4), 4)
        self.rect = self.image.get_rect(center=(x, y))
        self.mask = pygame.mask.from_surface(self.image)

        dx, dy = target_pos[0] - x, target_pos[1] - y
        distance = math.hypot(dx, dy)
        if distance == 0:
            distance = 1
        self.velocity = pygame.math.Vector2(dx / distance, dy / distance)
        self.speed = speed

    def update(self, dt):
        self.rect.x += self.velocity.x * self.speed * (dt / 1000)
        self.rect.y += self.velocity.y * self.speed * (dt / 1000)


        if self.rect.top > 600 or self.rect.bottom < 0 or self.rect.right < 0 or self.rect.left > 1000:
            self.kill()

    def render(self, screen):
        screen.blit(self.image, self.rect)
