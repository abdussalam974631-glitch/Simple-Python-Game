from entities.enemies.enemy_base import Enemy
from core.utils import Animations
import pygame
import math
from .serpent_segment import SerpentSegment

class SerpentHead(Enemy):
    def __init__(self, x, y, scene, length=8, spacing=12):
        super().__init__(Animations["serpenthead"], 40, 2, scene)

        self.position = pygame.math.Vector2(x, y)
        self.rect = self.image.get_rect(center=self.position)

        self.speed = 10
        self.wave_amplitude = 80     
        self.wave_speed = 2
        self.trail = []
        self.spacing = spacing

        # Create body segments
        self.segments = []
        for i in range(length):
            seg = SerpentSegment(scene, self)
            self.segments.append(seg)
            scene.enemies.add(seg)
            scene.all_sprites.add(seg)

        self.time = 0

    def unique_behaviour(self, dt):
        self.time += dt / 1000

        # Move head in a sine wave
        self.position.x = 500 + math.sin(self.time * self.wave_speed) * self.wave_amplitude
        self.position.y += self.speed * (dt / 1000)

        self.rect.center = (int(self.position.x), int(self.position.y))

        # Save head position to trail
        self.trail.insert(0, (self.position.x, self.position.y))
        if len(self.trail) > 300:
            self.trail.pop()

        # Kill when off screen
        if self.rect.top > 600:
            self.kill()
            for seg in self.segments:
                seg.kill()