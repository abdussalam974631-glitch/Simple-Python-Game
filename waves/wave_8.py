# waves/wave_8.py
from ._wave_base import Wave
from random import randint
from entities.enemies import SerpentHead, Evasive, Shooter, Burster
from entities.powerup import PowerUpSprite
from entities.powers import ExtraLife
from core.utils import HEALTH_IMG

class Wave8(Wave):
    def setup(self):
        
        self.stages = [
            (0,     self.stage_serpent),
            (10000,  self.stage_evasive_swarm),
            (2500,  self.stage_rest),
            (3000,  self.stage_shooters),
            (3500,  self.stage_burster_duo),
            (3000,  self.reward_stage)
        ]

    def stage_serpent(self):

        s = SerpentHead(500, -100, self.scene)
        self.scene.enemies.add(s)
        self.scene.all_sprites.add(s)
        self.enemies.append(s)

    def stage_evasive_swarm(self):
        positions = self.Fm.v_wave(4)
        for x, y in positions:
            e = Evasive(x, y, self.scene)
            self.scene.enemies.add(e)
            self.scene.all_sprites.add(e)
            self.enemies.append(e)

    def stage_shooters(self):
        positions = self.Fm.get_positions("line", count=3)
        for x, y in positions:
            s = Shooter(x, y, self.scene)
            self.scene.enemies.add(s)
            self.scene.all_sprites.add(s)
            self.enemies.append(s)

    def stage_burster_duo(self):

        left = (150, -80)
        right = (850, -80)
        b1 = Burster(left[0], left[1], self.scene)
        b2 = Burster(right[0], right[1], self.scene)
        self.scene.enemies.add(b1)
        self.scene.all_sprites.add(b1)
        self.enemies.append(b1)
        self.scene.enemies.add(b2)
        self.scene.all_sprites.add(b2)
        self.enemies.append(b2)

    def reward_stage(self):

        p = PowerUpSprite(HEALTH_IMG.copy(), ExtraLife, 500, -100)
        self.scene.powers.add(p)
        self.scene.all_sprites.add(p)
