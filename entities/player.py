import pygame
from core.utils import PLAYER_IMG, PLAYER_AREA
from core.utils import BULLET_SOUND
from core.utils import DEV_MODE
from . import bullets

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = PLAYER_IMG
        self.rect = self.image.get_rect(bottomleft=(0, 600))
        self.speed = 300
        self.shoot_delay = 250
        self.last_shot = 0
    
    def shoot(self, bullets_, all_sprites):
        now = pygame.time.get_ticks()
        if now - self.last_shot >= self.shoot_delay or DEV_MODE:
            self.last_shot = now
            BULLET_SOUND.play()
            bullet = bullets.Bullet(self.rect.midtop)
            bullets_.add(bullet)
            all_sprites.add(bullet)

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

        # Clamp to play area
        self.rect.clamp_ip(PLAYER_AREA)

    def update(self, dt):
        self.handle_input(dt)

    def render(self, screen):
        screen.blit(self.image, self.rect)
