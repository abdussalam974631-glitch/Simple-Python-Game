import random
import pygame
from .enemy import Enemy
from .bullets import EnemyBullet
from core.sound_manager import SoundManager
from core.utils import BASIC_IMG, EVASIVE_IMG, TANK_IMG, SHOOTER_IMG, DOPPELGANGER_IMG

class Basic(Enemy):
    def __init__(self, x=None, y=None, scene=None):
        super().__init__(BASIC_IMG, 50, 1, scene=scene)
        self.rect = self.image.get_rect(
            topleft=(x or random.randint(100, 900), y or random.randint(-100, 0))
        )
        self.position = pygame.math.Vector2(self.rect.topleft)
    
    def render(self, screen):
        screen.blit(self.image, self.rect)

class Evasive(Enemy):
    def __init__(self, x=None, y=None, scene=None):
        super().__init__(EVASIVE_IMG, 50, 1, scene=scene)
        self.rect = self.image.get_rect(
            topleft=(x or random.randint(100, 900), y or random.randint(-100, 0))
        )
        self.position = pygame.math.Vector2(self.rect.topleft)
        self.direction = 1
        self.projected_right = self.rect.right + 30
        self.projected_left = self.rect.left - 30
        

    def unique_behaviour(self, dt):
        self.position.x += self.direction * self.speed * (dt / 1000)
        if self.rect.right > self.projected_right and self.direction == abs(self.direction):
            self.direction *= -1
        if self.rect.left < self.projected_left and not (self.direction == abs(self.direction)):
            self.direction *= -1

    
    def render(self, screen):
        screen.blit(self.image, self.rect)

class Tank(Enemy):
    def __init__(self, x=None, y=None, scene=None):
        super().__init__(TANK_IMG, 30, 2, scene=scene)
        self.rect = self.image.get_rect(
            topleft=(x or random.randint(100, 900), y or random.randint(-100, 0))
        )
        self.position = pygame.math.Vector2(self.rect.topleft)
    
    def render(self, screen):
        screen.blit(self.image, self.rect)

class Shooter(Enemy):
    def __init__(self, x=None, y=None, scene=None):
        super().__init__(SHOOTER_IMG, 30, 2, scene=scene)
        self.rect = self.image.get_rect(
            topleft=(x or random.randint(100, 900), y or random.randint(-100, 0))
        )
        self.bullets = pygame.sprite.Group()
        self.position = pygame.math.Vector2(self.rect.topleft)
        self.shoot_delay = 2000
        self.last_shot = 0
    
    def unique_behaviour(self, dt):
        now = pygame.time.get_ticks()
        if now - self.last_shot >= self.shoot_delay:
            self.shoot_at_player()
            self.last_shot = now
        
        hits = pygame.sprite.groupcollide(self.bullets, pygame.sprite.GroupSingle(self.scene.player), True, False, collided=pygame.sprite.collide_mask)
        for power, x in hits.items():
            self.scene.player.lives = max(0, self.scene.player.lives - 1)        

    def shoot_at_player(self):
        target = self.scene.player.rect.center
        bullet = EnemyBullet(self.rect.centerx, self.rect.bottom, target)
        SoundManager.play("enemy_bullet")
        self.bullets.add(bullet)
        self.scene.all_sprites.add(bullet)
        

    def render(self, screen):
        screen.blit(self.image, self.rect)