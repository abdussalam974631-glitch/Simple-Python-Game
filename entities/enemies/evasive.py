from .enemy_base import Enemy
from core.utils import Animations
import random, pygame

class Evasive(Enemy):
    def __init__(self, x=None, y=None, scene=None):
        super().__init__(Animations["evasive"], 50, 1, scene=scene)
        self.rect = self.image.get_rect(
            topleft=(x or random.randint(100, 900), y or random.randint(-100, 0))
        )
        self.position = pygame.math.Vector2(self.rect.topleft)
        self.direction = 1
        self.projected_right = self.rect.right + 30
        self.projected_left = self.rect.left - 30
        

    def unique_behaviour(self, dt):
        self.position.x += self.direction * self.speed * (dt / 1000)
        if self.rect.right > self.projected_right and self.direction == abs(self.direction):
            self.direction *= -1
        if self.rect.left < self.projected_left and not (self.direction == abs(self.direction)):
            self.direction *= -1

    
    def render(self, screen):
        screen.blit(self.image, self.rect)