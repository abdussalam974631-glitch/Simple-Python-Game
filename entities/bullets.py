import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos, speed=-500):
        super().__init__()
        self.image = pygame.Surface((8, 8), pygame.SRCALPHA)
        pygame.draw.circle(self.image, (255, 0, 0), (4, 4), 4)
        self.rect = self.image.get_rect(center=pos)
        self.speed = speed

    def update(self, dt):
        self.rect.y += self.speed * (dt / 1000)
        if self.rect.bottom < 0:
            self.kill()
