# core/waves/wave_1.py
from ._wave_base import Wave
from random import randint
from entities.enemies import Basic, Evasive
from entities.powerup import PowerUpSprite
from core.utils import HEALTH_IMG
from entities.powers import ExtraLife


class Wave3(Wave):
    def setup(self):
        self.stages = [
            (0, self.stage_1),        
            (3500, self.stage_2),     
            (4500, self.stage_3),     
            (3000, self.stage_rest)   
        ]

    def stage_1(self):
        positions = self.Fm.get_positions("slant_right", count=4, start_x=200)
        for pos in positions:
            enemy = Basic(pos[0], pos[1], self.scene)
            self.scene.enemies.add(enemy)
            self.scene.all_sprites.add(enemy)
            self.enemies.append(enemy)


    def stage_2(self):
        positions = self.Fm.get_positions("slant_left", count=4, start_x=700)
        for pos in positions:
            enemy = Basic(pos[0], pos[1], self.scene)
            self.scene.enemies.add(enemy)
            self.scene.all_sprites.add(enemy)
            self.enemies.append(enemy)


    def stage_3(self):
        positions = self.Fm.get_positions("line", count=5)
        for pos in positions:
            enemy = Basic(pos[0], pos[1], self.scene)
            self.scene.enemies.add(enemy)
            self.scene.all_sprites.add(enemy)
            self.enemies.append(enemy)


        # 50% chance powerup drop
        if randint(0, 1):
            p = PowerUpSprite(HEALTH_IMG.copy(), ExtraLife, 500, -100)
            self.scene.powers.add(p)
            self.scene.all_sprites.add(p)