import random
import pygame
from entities.enemies.enemy_base import Enemy
from core.utils import Animations

class Teleporter(Enemy):
    def __init__(self, x, y, scene):
        super().__init__(Animations["basic"], 90, 2, scene=scene)
        self.rect = self.image.get_rect(
            topleft=(x or random.randint(100, 900), y or random.randint(-120, -40))
        )
        self.position = pygame.math.Vector2(self.rect.topleft)
        
        self.teleport_timer = 0
        self.teleport_interval = random.randint(1200, 2000)
        self.teleport_cooldown = 300

        self.is_teleporting = False
        self.teleport_pause_timer = 0

    def unique_behaviour(self, dt):
        if self.is_teleporting:
            self.teleport_pause_timer += dt
            if self.teleport_pause_timer >= self.teleport_cooldown:
                self.perform_teleport()
            return


        self.teleport_timer += dt
        if self.teleport_timer >= self.teleport_interval:
            self.start_teleport()

    def start_teleport(self):

        self.is_teleporting = True
        self.teleport_pause_timer = 0

    def perform_teleport(self):

        self.is_teleporting = False
        self.teleport_timer = 0
        self.teleport_interval = random.randint(1400, 2200)

        new_x = random.randint(50, 1000 - 50)
        new_y = random.randint(0, 600 // 2)

        self.position = pygame.math.Vector2(new_x, new_y)

