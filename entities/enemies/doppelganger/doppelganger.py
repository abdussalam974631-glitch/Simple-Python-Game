from entities.enemies.enemy_base import Enemy
from core.utils import Animations
import random, pygame
from core.sound_man import SoundManager
from .doppelganger_clone import DoppelgangerClone

class Doppelganger(Enemy):
    def __init__(self, x=None, y=None, scene=None):
        super().__init__(Animations["doppelganger"], 20, 1, scene=scene)
        self.rect = self.image.get_rect(
            topleft=(x or random.randint(100, 900),
                     y or random.randint(-100, 0))
        )
        self.position = pygame.math.Vector2(self.rect.topleft)

        # Duplication properties
        self.spacing = 0
        self.clones = pygame.sprite.Group()

        self.last_duplication = 0
        self.duplicate_delay = 2000  # ms
        self.max_clones = 4

    def unique_behaviour(self, dt):
        now = pygame.time.get_ticks()
        if now - self.last_duplication >= self.duplicate_delay and len(self.clones) < self.max_clones:
            self.spawn_clone()
            self.last_duplication = now
        elif now - self.last_duplication >= self.duplicate_delay:
            self.last_duplication = now

    def spawn_clone(self):
        """Create a new clone offset to left/right alternately."""
        self.spacing = self.spacing + 75 if len(self.clones) % 2 == 0 else self.spacing
        direction = -1 if len(self.clones) % 2 == 0 else 1
        offset = direction * self.spacing
        clone_x = self.rect.x + offset
        clone_y = self.rect.y
        clone = DoppelgangerClone(clone_x, clone_y, self.scene, parent=self)
        self.clones.add(clone)
        self.scene.enemies.add(clone)
        self.scene.all_sprites.add(clone)

    def take_damage(self, amount):
        """Randomly kill one of the doppelgangers (self or clone)."""
        all_entities = [self] + list(self.clones)
        if all_entities:
            victim = random.choice(all_entities)
            victim.die()

    def die(self):
        """Destroy self and all clones."""
        SoundManager.play("square_death")
        for clone in list(self.clones):
            clone.kill()
        self.kill()