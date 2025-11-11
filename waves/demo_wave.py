from .wave_base import Wave
from random import randint
from entities.enemies import Evasive
from entities.powerup import PowerUpSprite
from core.utils import HEALTH_IMG
from entities.powers import ExtraLife

class Demo_Wave(Wave):
    def setup(self):
        self.stages = [
            (0, self.stage_1)
        ]

    def stage_1(self):
        positions = [(500, -100)]
        for pos in positions:
            enemy = Evasive(pos[0], pos[1], self.scene)
            self.scene.enemies.add(enemy)
            self.scene.all_sprites.add(enemy)
            self.enemies.append(enemy)