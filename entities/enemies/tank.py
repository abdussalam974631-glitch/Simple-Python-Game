import pygame, random
from .enemy_base import Enemy
from core.utils import Animations

class Tank(Enemy):
    def __init__(self, x=None, y=None, scene=None):
        super().__init__(Animations["tank"], 30, 2, scene=scene)
        self.rect = self.image.get_rect(
            topleft=(x or random.randint(100, 900), y or random.randint(-100, 0))
        )
        self.position = pygame.math.Vector2(self.rect.topleft)
    
    def render(self, screen):
        screen.blit(self.image, self.rect)
