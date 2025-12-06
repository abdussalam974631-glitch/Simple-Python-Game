# waves/wave_6.py
from ._wave_base import Wave
from random import randint
from entities.enemies import Basic, Evasive, Burster
from entities.powerup import PowerUpSprite
from entities.powers import ExtraLife
from core.utils import HEALTH_IMG

class Wave6(Wave):
    def setup(self):

        self.stages = [
            (0,     self.stage_intro_line),
            (3500,  self.stage_evasive_pressure),
            (5000,  self.stage_rest),
            (5000,  self.stage_burster_intro),
            (5000,  self.reward_stage)
        ]

    def stage_intro_line(self):
        positions = self.Fm.get_positions("slant_right", count=3, start_x=150)
        for x, y in positions:
            e = Basic(x, y, self.scene)
            self.scene.enemies.add(e)
            self.scene.all_sprites.add(e)
            self.enemies.append(e)

    def stage_evasive_pressure(self):
        positions = self.Fm.get_positions("slant_left", count=3, start_x=700)
        for x, y in positions:
            e = Evasive(x, y, self.scene)
            # slightly faster evasives for a gentle bump
            e.speed *= 1.15
            self.scene.enemies.add(e)
            self.scene.all_sprites.add(e)
            self.enemies.append(e)

    def stage_burster_intro(self):

        pos = (self.Fm.W // 2, -80)
        b = Burster(pos[0], pos[1], self.scene)
        self.scene.enemies.add(b)
        self.scene.all_sprites.add(b)
        self.enemies.append(b)

    def reward_stage(self):
        
        p = PowerUpSprite(HEALTH_IMG.copy(), ExtraLife, 500, -100)
        self.scene.powers.add(p)
        self.scene.all_sprites.add(p)
