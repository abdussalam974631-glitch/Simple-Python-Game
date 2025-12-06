# waves/wave_7.py
from ._wave_base import Wave
from random import randint
from entities.enemies import Basic, Cloaker, Teleporter, Evasive
from entities.powerup import PowerUpSprite
from entities.powers import ExtraLife, RapidFire
from core.utils import HEALTH_IMG

class Wave7(Wave):
    def setup(self):
        # Foreshadowing wave: introduce cloakers and a teleporter teaser
        self.stages = [
            (0,    self.stage_basic_opener),
            (4000, self.stage_cloakers),
            (3000, self.stage_rest),
            (3000, self.stage_teleporter_tease),
            (3500, self.stage_mixed_evasive),
            (3000, self.optional_reward)
        ]

    def stage_basic_opener(self):
        positions = self.Fm.get_positions("line", count=4)
        for x, y in positions:
            e = Basic(x, y, self.scene)
            self.scene.enemies.add(e)
            self.scene.all_sprites.add(e)
            self.enemies.append(e)

    def stage_cloakers(self):
        positions = self.Fm.get_positions("slant_right", count=2, start_x=250)
        for x, y in positions:
            c = Cloaker(x, y, self.scene)
            self.scene.enemies.add(c)
            self.scene.all_sprites.add(c)
            self.enemies.append(c)

    def stage_teleporter_tease(self):
        x, y = 500, -100
        t = Teleporter(x, y, self.scene)
        self.scene.enemies.add(t)
        self.scene.all_sprites.add(t)
        self.enemies.append(t)

    def stage_mixed_evasive(self):
        positions = self.Fm.get_positions("slant_left", count=3, start_x=700)
        for x, y in positions:
            e = Evasive(x, y, self.scene)
            e.speed *= 1.1
            self.scene.enemies.add(e)
            self.scene.all_sprites.add(e)
            self.enemies.append(e)

    def optional_reward(self):
        if randint(0, 1):
            p = PowerUpSprite(HEALTH_IMG.copy(), ExtraLife, 500, -100)
            self.scene.powers.add(p)
            self.scene.all_sprites.add(p)
        else:
            # 30% chance of RapidFire instead
            if randint(0, 9) < 3:
                p2 = PowerUpSprite(HEALTH_IMG.copy(), RapidFire, 500, -100)
                self.scene.powers.add(p2)
                self.scene.all_sprites.add(p2)
