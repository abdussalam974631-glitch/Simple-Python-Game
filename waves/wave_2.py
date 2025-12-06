# core/waves/wave_1.py
from ._wave_base import Wave
from random import randint
from entities.enemies import Basic, Evasive
from entities.powerup import PowerUpSprite
from core.utils import HEALTH_IMG
from entities.powers import ExtraLife


class Wave2(Wave):
    def setup(self):
        self.stages = [
            (0,     self.spawn_slant_right_group),
            (5000,  self.stage_rest),   
            (9000,  self.spawn_slant_left_group),
            (13000, self.optional_reward),
            (17000, self.stage_rest)    
        ]

    def spawn_slant_right_group(self):
        positions = self.Fm.get_positions("slant_right", count=3, start_x=250)
        for pos in positions:
            enemy = Basic(pos[0], pos[1], self.scene)
            self.scene.enemies.add(enemy)
            self.scene.all_sprites.add(enemy)
            self.enemies.append(enemy)

    def spawn_slant_left_group(self):
        positions = self.Fm.get_positions("slant_left", count=3, start_x=750)
        for pos in positions:
            e = Evasive(pos[0], pos[1], self.scene)
            self.scene.enemies.add(e)
            self.scene.all_sprites.add(e)
            self.enemies.append(e)

    def optional_reward(self):
        if randint(0, 1):
            p = PowerUpSprite(HEALTH_IMG.copy(), ExtraLife, 500, -100)
            self.scene.powers.add(p)
            self.scene.all_sprites.add(p)