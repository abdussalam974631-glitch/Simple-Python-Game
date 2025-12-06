from .enemy_base import Enemy
from core.utils import Animations
import pygame
import random
from core.sound_man import SoundManager
from entities.bullets.enemy_bullet.enemy_bullet_vector import EnemyBulletVector

class Burster(Enemy):
    def __init__(self, x=None, y=None, scene=None):
        super().__init__(Animations["burster"], 200, 1, scene=scene)
        self.rect = self.image.get_rect(
            topleft=(x or random.randint(100, 900),
                     y or random.randint(-100, 0))
        )
        self.position = pygame.math.Vector2(self.rect.topleft)

    def render(self, screen):
        screen.blit(self.image, self.rect)

    def check_bounds(self):
        pass

    def unique_behaviour(self, dt):
        if self.rect.bottom > 590:
            SoundManager.play("burster_death")
            self.explode()
            self.kill()

    def explode(self):
        cx, cy = self.rect.center

        # 5-way burst directions
        dirs = [
            (0, -1),
            (0.7, -1),
            (-0.7, -1),
            (0.4, -1),
            (-0.4, -1),
        ]

        for d in dirs:
            bullet = EnemyBulletVector(cx, cy, pygame.math.Vector2(d))
            self.scene.enemy_bullets.add(bullet)
            self.scene.all_sprites.add(bullet)