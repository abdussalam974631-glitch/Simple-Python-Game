import pygame, random
from core.utils import BASIC_IMG, EVASIVE_IMG, TANK_IMG

class Basic(pygame.sprite.Sprite):
    def __init__(self, x=None, y=None):
        super().__init__()
        self.image = BASIC_IMG
        self.rect = self.image.get_rect(
            topleft=(x or random.randint(100, 900), y or random.randint(-100, 0))
        )
        self.speed = 50
        self.health = 1
        

    def update(self, dt):
        self.rect.y += self.speed * (dt / 1000)

    
    def render(self, screen):
        screen.blit(self.image, self.rect)

class Evasive(pygame.sprite.Sprite):
    def __init__(self, x=None, y=None):
        super().__init__()
        self.image = EVASIVE_IMG
        self.rect = self.image.get_rect(
            topleft=(x or random.randint(100, 900), y or random.randint(0, 100))
        )
        self.speed = 50
        self.health = 1
        self.direction = random.choice([-1, 1])
        self.projected_right = self.rect.right + 30
        self.projected_left = self.rect.left - 30
        

    def update(self, dt):
        self.rect.y += self.speed * (dt / 1000)
        self.rect.x += self.direction * self.speed * (dt / 1000)
        if self.rect.left <= self.projected_left or self.rect.right >= self.projected_right:
            self.direction *= -1

    
    def render(self, screen):
        screen.blit(self.image, self.rect)

class Tank(pygame.sprite.Sprite):
    def __init__(self, x=None, y=None):
        super().__init__()
        self.image = TANK_IMG
        self.rect = self.image.get_rect(
            topleft=(x or random.randint(100, 900), y or random.randint(-100, 0))
        )
        self.speed = 30
        self.health = 3
        

    def update(self, dt):
        self.rect.y += self.speed * (dt / 1000)

    
    def render(self, screen):
        screen.blit(self.image, self.rect)