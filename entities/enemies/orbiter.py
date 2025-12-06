from .enemy_base import Enemy
from core.utils import Animations
import pygame
import math

class Orbiter(Enemy):
    def __init__(self, center_x, center_y, radius, angle, scene, angular_speed=1.5, drift_speed=40):
        super().__init__(Animations["orbiter"], 0, 1, scene)

        # Orbit parameters
        self.center = pygame.math.Vector2(center_x, center_y)
        self.radius = radius
        self.angle = angle  # in radians
        self.angular_speed = angular_speed  # radians/sec
        self.drift_speed = drift_speed  # downward drift

        # Initial position
        self.position = pygame.math.Vector2(
            self.center.x + math.cos(self.angle) * self.radius,
            self.center.y + math.sin(self.angle) * self.radius
        )
        self.rect = self.image.get_rect(center=self.position)

    def unique_behaviour(self, dt):
        # Update orbit angle
        self.angle += self.angular_speed * (dt / 1000)

        # Drift the orbit center slowly down
        self.center.y += self.drift_speed * (dt / 1000)

        # Recalculate orbit position
        self.position.x = self.center.x + math.cos(self.angle) * self.radius
        self.position.y = self.center.y + math.sin(self.angle) * self.radius

        self.rect.center = (int(self.position.x), int(self.position.y))

        # Remove when below screen
        if self.rect.top > 600:
            self.kill()