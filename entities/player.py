import pygame
from core.sound_manager import SoundManager
from core.utils import PLAYER_IMG, PLAYER_AREA
from core.utils import DEV_MODE
from . import bullets

class Player(pygame.sprite.Sprite):
    def __init__(self, scene):
        super().__init__()
        self.scene = scene
        self.image = PLAYER_IMG
        self.rect = self.image.get_rect(bottomleft=(0, 600))
        self.mask = pygame.mask.from_surface(self.image)
        self.lives = 5
        self.active_powerups = []
        self.speed = 300
        self.shoot_delay = 400
        self.last_shot = 0
    
    def shoot(self, bullets_, all_sprites):
        now = pygame.time.get_ticks()
        if now - self.last_shot >= self.shoot_delay or DEV_MODE:
            self.last_shot = now
            SoundManager.play("shoot")
            bullet = bullets.Bullet(self.rect.midtop)
            bullets_.add(bullet)
            all_sprites.add(bullet)

    def add_powerup(self, powerup):
        powerup.apply(self)
        if powerup.duration > 0:
            self.active_powerups.append(powerup)

    def update_powerups(self):

        self.active_powerups = [
            p for p in self.active_powerups if p.update(self)
        ]

    def handle_input(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.rect.y -= self.speed * (dt / 1000)
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed * (dt / 1000)
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed * (dt / 1000)
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed * (dt / 1000)

        if self.lives <= 0:
            self.scene.exit()

        # Clamp to play area
        self.rect.clamp_ip(PLAYER_AREA)

    def update(self, dt):
        self.handle_input(dt)

    def render(self, screen):
        screen.blit(self.image, self.rect)
