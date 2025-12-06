import pygame
from .enemy_base import Enemy
from core.utils import Animations
import random

class Cloaker(Enemy):
    def __init__(self, x=None, y=None, scene=None):
        super().__init__(Animations["cloaker"], 40, 2, scene=scene)
        self.rect = self.image.get_rect(
            topleft=(x or random.randint(100, 900), y or random.randint(-120, -40))
        )
        self.position = pygame.math.Vector2(self.rect.topleft)

        self.visible = True
        self.toggle_delay = 2000  # ms
        self.last_toggle = pygame.time.get_ticks()

    def unique_behaviour(self, dt):
        now = pygame.time.get_ticks()

        if now - self.last_toggle >= self.toggle_delay:
            self.visible = not self.visible
            self.last_toggle = now

            if self.visible:
                from core.animation import Animation
                self.animation = Animation(Animations["cloaker"])
            else:
                # invisible version
                self.animation = Animation([pygame.Surface((0,0), pygame.SRCALPHA)])
            
            self.image = self.animation.get_frame().copy()
            self.mask = pygame.mask.from_surface(self.image)


    def render(self, screen):
        if self.visible:
            screen.blit(self.image, self.rect)