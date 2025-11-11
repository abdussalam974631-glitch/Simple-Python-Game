from .wave_base import Wave
from entities.enemies import *

class Wave5(Wave):
    def setup(self):
        self.stages = [
            (0, self.stage_1),
            (1000, self.stage_2),
            (5000, self.stage_3),
            (1000, self.stage_4),
            (5000, self.stage_5),
            (1000, self.stage_6)
        ]

    def stage_1(self):
        positions = self.Fm.get_positions("slant_right", count=3, start_x=250)
        for pos in positions:
            enemy = Basic(pos[0], pos[1], self.scene)
            self.scene.enemies.add(enemy)
            self.scene.all_sprites.add(enemy)
            self.enemies.append(enemy)
    
    def stage_2(self):
        positions = self.Fm.get_positions("slant_right", count=3, start_x=250)
        for pos in positions:
            enemy = Shooter(pos[0], pos[1], self.scene)
            self.scene.enemies.add(enemy)
            self.scene.all_sprites.add(enemy)
            self.enemies.append(enemy)
    
    def stage_3(self):
        positions = self.Fm.get_positions("slant_right", count=3, start_x=500)
        for pos in positions:
            enemy = Basic(pos[0], pos[1], self.scene)
            self.scene.enemies.add(enemy)
            self.scene.all_sprites.add(enemy)
            self.enemies.append(enemy)
    
    def stage_4(self):
        positions = self.Fm.get_positions("slant_right", count=3, start_x=500)
        for pos in positions:
            enemy = Shooter(pos[0], pos[1], self.scene)
            self.scene.enemies.add(enemy)
            self.scene.all_sprites.add(enemy)
            self.enemies.append(enemy)
    
    def stage_5(self):
        positions = self.Fm.get_positions("slant_right", count=3, start_x=750)
        for pos in positions:
            enemy = Basic(pos[0], pos[1], self.scene)
            self.scene.enemies.add(enemy)
            self.scene.all_sprites.add(enemy)
            self.enemies.append(enemy)
    
    def stage_6(self):
        positions = self.Fm.get_positions("slant_right", count=3, start_x=750)
        for pos in positions:
            enemy = Shooter(pos[0], pos[1], self.scene)
            self.scene.enemies.add(enemy)
            self.scene.all_sprites.add(enemy)
            self.enemies.append(enemy)