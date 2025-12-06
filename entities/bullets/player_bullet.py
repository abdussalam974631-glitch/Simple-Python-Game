import pygame
from core.animation import Animation
from core.utils import BULLET_FRAMES

class player_bullet(pygame.sprite.Sprite):
    def __init__(self, pos, speed=-500):
        super().__init__()
        self.frames = BULLET_FRAMES
        self.animation = Animation(self.frames, frame_duration=100)
        self.image = self.animation.get_frame()
        self.rect = self.image.get_rect(center=pos)
        self.mask = pygame.mask.from_surface(self.image)
        self.speed = speed

    def update(self, dt):
        self.rect.y += self.speed * (dt / 1000)
        self.animation.update(dt)
        self.image = self.animation.get_frame()
        if self.rect.bottom < 0:
            self.kill()