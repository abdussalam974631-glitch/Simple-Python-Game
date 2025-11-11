# entities/powerup.py
import pygame
import random

class PowerUpSprite(pygame.sprite.Sprite):
    def __init__(self, image, powerup_class, x=None, y=None):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(
            center=(x or random.randint(100, 900), y or random.randint(-100, 0))
        )
        self.powerup_class = powerup_class  
        self.speed = 50

    def update(self, dt):
        self.rect.y += self.speed * (dt / 1000)
        if self.rect.top > 600:
            self.kill()

    def apply_to_player(self, player):
        powerup = self.powerup_class()
        player.add_powerup(powerup)
        self.kill()

