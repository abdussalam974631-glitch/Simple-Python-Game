# core/waves/wave_1.py
from ._wave_base import Wave
from random import randint
from entities.enemies import Basic
from entities.powerup import PowerUpSprite
from core.utils import HEALTH_IMG
from entities.powers import ExtraLife

class Wave1(Wave):
    def setup(self):
        self.stages = [
            (0, self.spawn_intro_group),
            (4000, self.stage_rest),
            (8000, self.spawn_single_enemy),
            (12000, self.spawn_reward),
            (16000, self.stage_rest)
        ]

    def spawn_intro_group(self):
        positions = self.Fm.get_positions("line", count=3)
        for pos in positions:
            enemy = Basic(pos[0], pos[1], self.scene)
            self.scene.enemies.add(enemy)
            self.scene.all_sprites.add(enemy)
            self.enemies.append(enemy)

    def spawn_single_enemy(self):
        positions = self.Fm.get_positions("line", count=1)
        for pos in positions:
            enemy = Basic(pos[0], pos[1], self.scene)
            self.scene.enemies.add(enemy)
            self.scene.all_sprites.add(enemy)
            self.enemies.append(enemy)

    def spawn_reward(self):
        Xtralife = PowerUpSprite(HEALTH_IMG.copy(), ExtraLife, 500, -100)
        self.scene.powers.add(Xtralife)
        self.scene.all_sprites.add(Xtralife)
        
        