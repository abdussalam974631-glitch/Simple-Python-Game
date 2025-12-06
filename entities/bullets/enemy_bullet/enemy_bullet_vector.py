import pygame

class EnemyBulletVector(pygame.sprite.Sprite):
    def __init__(self, x, y, direction, speed=220):
        super().__init__()
        self.image = pygame.Surface((8, 8), pygame.SRCALPHA)
        pygame.draw.circle(self.image, (255, 80, 80), (4, 4), 4)
        self.rect = self.image.get_rect(center=(x, y))
        self.mask = pygame.mask.from_surface(self.image)

        self.velocity = pygame.math.Vector2(direction).normalize()
        self.speed = speed

        self.pos = pygame.math.Vector2(self.rect.center)

    def update(self, dt):
        self.pos += self.velocity * (self.speed * dt / 1000)
        self.rect.center = (int(self.pos.x), int(self.pos.y))

        if (self.rect.top > 600 or self.rect.bottom < 0 or 
            self.rect.right < 0 or self.rect.left > 1000):
            self.kill()