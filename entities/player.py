import pygame
from core.sound_man import SoundManager
from core.animation import Animation
from core.utils import PLAYER_STATES, PLAYER_AREA
from core.utils import DEV_MODE
from .bullets import player_bullet

class Player(pygame.sprite.Sprite):
    def __init__(self, scene):
        super().__init__()
        self.scene = scene
        self.sprites = PLAYER_STATES
        self.lives = 5
        self.animation = Animation(self.sprites[self.lives])
        self.image = self.animation.get_frame()
        self.rect = self.image.get_rect(bottomleft=(0, 600))
        self.mask = pygame.mask.from_surface(self.image)
        self.active_powerups = []
        self.speed = 300
        self.shoot_delay = 400
        self.last_shot = 0
    
    def shoot(self, bullets_, all_sprites):
        now = pygame.time.get_ticks()
        if now - self.last_shot >= self.shoot_delay or DEV_MODE:
            self.last_shot = now
            SoundManager.play("shoot")
            bullet = player_bullet.player_bullet(self.rect.midtop)
            bullets_.add(bullet)
            all_sprites.add(bullet)

    def take_damage(self):
        self.scene.ui_manager.on_lives_changed(max(0, self.lives - 1))
        self.lives = max(0, self.lives - 1)
        self.update_image()
    
    def gain_life(self):
        self.scene.ui_manager.on_lives_changed(min(5, self.lives + 1))
        self.lives = min(5, self.lives + 1)
        self.update_image()

    def update_image(self):
        self.lives = max(1, min(self.lives, 5))
        self.animation = Animation(self.sprites[self.lives])
        self.image = self.animation.get_frame()
          

    def add_powerup(self, powerup):
        powerup.apply(self)
        self.update_image()
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
        self.animation.update(dt)
        self.image = self.animation.get_frame()

    def render(self, screen):
        screen.blit(self.image, self.rect)
