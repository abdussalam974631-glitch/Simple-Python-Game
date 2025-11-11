# core/waves/wave_1.py
from .wave_base import Wave
from random import randint
from entities.enemies import Basic, Evasive
from entities.powerup import PowerUpSprite
from core.utils import HEALTH_IMG
from entities.powers import ExtraLife


class Wave2(Wave):
    def setup(self):
        self.stages = [
            (0, self.stage_1),
            (5000, self.stage_2),
            (5000, self.stage_3),
            (5000, self.stage_4)
        ]

    def stage_1(self):
        positions = self.Fm.get_positions("slant_left", count=3, start_x=750)
        for pos in positions:
            enemy = Basic(pos[0], pos[1], self.scene)
            self.scene.enemies.add(enemy)
            self.scene.all_sprites.add(enemy)
            self.enemies.append(enemy)

    def stage_2(self):
        positions = self.Fm.get_positions("slant_left", count=3, start_x=500)
        for pos in positions:
            enemy = Basic(pos[0], pos[1], self.scene)
            self.scene.enemies.add(enemy)
            self.scene.all_sprites.add(enemy)
            self.enemies.append(enemy)

    def stage_3(self):
        positions = self.Fm.get_positions("slant_left", count=3, start_x=250)
        for pos in positions:
            enemy = Basic(pos[0], pos[1], self.scene)
            self.scene.enemies.add(enemy)
            self.scene.all_sprites.add(enemy)
            self.enemies.append(enemy)
    
        if randint(0, 1):
            Xtralife = PowerUpSprite(HEALTH_IMG.copy(), ExtraLife, 500, -100)
            self.scene.powers.add(Xtralife)
            self.scene.all_sprites.add(Xtralife)

    def stage_4(self):
        positions = self.Fm.get_positions("line", count=3)
        for pos in positions:
            enemy = Evasive(pos[0], pos[1], self.scene)
            self.scene.enemies.add(enemy)
            self.scene.all_sprites.add(enemy)
            self.enemies.append(enemy)