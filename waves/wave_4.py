# core/waves/wave_1.py
from ._wave_base import Wave
from random import randint
from entities.enemies import Basic

class Wave4(Wave):
    def setup(self):
        self.stages = [
            (0, self.stage_1),
            (3500, self.stage_2),
            (4000, self.stage_rest),    # empty 4 seconds
            (3500, self.stage_3),
            (4000, self.stage_4)
        ]

    def stage_1(self):
        positions = self.Fm.get_positions("slant_left", 4, start_x=750)
        for pos in positions:
            enemy = Basic(pos[0], pos[1], self.scene)
            self.scene.enemies.add(enemy)
            self.scene.all_sprites.add(enemy)
            self.enemies.append(enemy)


    def stage_2(self):
        positions = self.Fm.get_positions("slant_left", 4, start_x=450)
        for pos in positions:
            enemy = Basic(pos[0], pos[1], self.scene)
            self.scene.enemies.add(enemy)
            self.scene.all_sprites.add(enemy)
            self.enemies.append(enemy)


    def stage_3(self):
        positions = self.Fm.get_positions("v_wave", 5)  # vertical gentle wave
        for pos in positions:
            enemy = Basic(pos[0], pos[1], self.scene)
            self.scene.enemies.add(enemy)
            self.scene.all_sprites.add(enemy)
            self.enemies.append(enemy)


    def stage_4(self):
        positions = self.Fm.get_positions("line", 3)
        for pos in positions:
            enemy = Basic(pos[0], pos[1], self.scene)
            self.scene.enemies.add(enemy)
            self.scene.all_sprites.add(enemy)
            self.enemies.append(enemy)
