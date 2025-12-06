from ._wave_base import Wave
from entities.enemies import *
from random import randint

class Demo_Wave(Wave):
    def setup(self):
        self.stages = [
            (0, self.stage_1),
            (10000, self.stage_2)
        ]

    def stage_1(self):
        positions = self.Fm.get_positions("line", 2)
        for pos in positions:
            enemy = Cloaker(pos[0], pos[1], self.scene)
            self.scene.enemies.add(enemy)
            self.scene.all_sprites.add(enemy)
            self.enemies.append(enemy)
    
    def stage_2(self):
        pass