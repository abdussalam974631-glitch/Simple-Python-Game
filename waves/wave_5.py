# core/waves/wave_1.py
from ._wave_base import Wave
from entities.enemies import Basic, Shooter
from entities.powerup import PowerUpSprite
from core.utils import HEALTH_IMG
from entities.powers import ExtraLife

class Wave5(Wave):
    def setup(self):
        self.stages = [
            (0, self.stage_1),
            (3200, self.stage_2),
            (4000, self.stage_rest),   # calm before shooters
            (3000, self.stage_3),
            (3500, self.stage_4),
            (4000, self.reward_stage)
        ]

    def stage_1(self):
        positions = self.Fm.get_positions("slant_right", 4, start_x=200)
        for pos in positions:
            enemy = Basic(pos[0], pos[1], self.scene)
            self.scene.enemies.add(enemy)
            self.scene.all_sprites.add(enemy)
            self.enemies.append(enemy)

    def stage_2(self):
        positions = self.Fm.get_positions("slant_right", 3, start_x=500)
        for pos in positions:
            enemy = Basic(pos[0], pos[1], self.scene)
            self.scene.enemies.add(enemy)
            self.scene.all_sprites.add(enemy)
            self.enemies.append(enemy)

    def stage_3(self):
        positions = self.Fm.get_positions("line", 3)
        for pos in positions:
            enemy = Shooter(pos[0], pos[1], self.scene)
            self.scene.enemies.add(enemy)
            self.scene.all_sprites.add(enemy)
            self.enemies.append(enemy)

    def stage_4(self):
        positions = self.Fm.get_positions("v_wave", 5)
        for pos in positions:
            enemy = Shooter(pos[0], pos[1], self.scene)
            self.scene.enemies.add(enemy)
            self.scene.all_sprites.add(enemy)
            self.enemies.append(enemy)

    def reward_stage(self):
        p = PowerUpSprite(HEALTH_IMG.copy(), ExtraLife, 500, -100)
        self.scene.powers.add(p)
        self.scene.all_sprites.add(p)
