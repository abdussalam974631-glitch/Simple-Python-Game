from entities.enemies.enemy_base import Enemy
from core.utils import Animations
import pygame

class SerpentSegment(Enemy):
    def __init__(self, scene, head):
        super().__init__(Animations["serpentsegment"], 30, 1, scene)
        self.head = head
        self.index_offset = len(self.head.segments) * head.spacing
        self.position = pygame.math.Vector2(head.position)
        self.rect = self.image.get_rect(center=self.position)

    def unique_behaviour(self, dt):
        # Follow trail if enough positions exist
        trail = self.head.trail

        if len(trail) > self.index_offset:
            tx, ty = trail[self.index_offset]
            self.position.x = tx
            self.position.y = ty
            self.rect.center = (int(tx), int(ty))

        # Kill if head is gone
        if not self.head.alive():
            self.kill()