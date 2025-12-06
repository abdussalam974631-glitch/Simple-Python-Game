from core.utils import Animations
import pygame, random
from .enemy_base import Enemy
from core.sound_man import SoundManager
from entities.bullets.enemy_bullet.enemy_bullet_aimed import EnemyBulletAimed

class Shooter(Enemy):
    def __init__(self, x=None, y=None, scene=None):
        super().__init__(Animations["shooter"], 30, 1, scene=scene)
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
            self.scene.player.take_damage()     

    def shoot_at_player(self):
        target = self.scene.player.rect.center
        bullet = EnemyBulletAimed(self.rect.centerx, self.rect.bottom, target)
        SoundManager.play("enemy_bullet")
        self.bullets.add(bullet)
        self.scene.all_sprites.add(bullet)
        

    def render(self, screen):
        screen.blit(self.image, self.rect)