from entities.enemies.enemy_base import Enemy
from core.utils import Animations
import pygame

class DoppelgangerClone(Enemy):
    def __init__(self, x, y, scene=None, parent=None):
        super().__init__(Animations["doppelganger"], 20, 1, scene=scene)
        self.parent = parent
        self.rect = self.image.get_rect(topleft=(x, y))
        self.position = pygame.math.Vector2(self.rect.topleft)

    def unique_behaviour(self, dt):
        # Descending handled by Enemy.update()
        pass

    def take_damage(self, amount):
        """Forward hits to the parent (parent decides who dies)."""
        if self.parent:
            self.parent.take_damage(amount)