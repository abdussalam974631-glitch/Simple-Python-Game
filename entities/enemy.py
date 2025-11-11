# entities/enemy.py
import pygame
from core.sound_manager import SoundManager

class Enemy(pygame.sprite.Sprite):
    def __init__(self, image, speed, health, scene):
        super().__init__()
        self.image = image.copy()
        self.mask = pygame.mask.from_surface(self.image)
        self.speed = speed
        self.health = health
        self.scene = scene  
        self.flash_timer = 0
        self.flash_duration = 100
        self.is_flashing = False
        self.velocity = pygame.math.Vector2(0, 1)

    def take_damage(self, amount):
        self.health -= amount
        self.flash_white()

        if self.health <= 0:
            self.die()

    def flash_white(self):
        if not self.is_flashing:
            self.original_image = self.image.copy()
        white_overlay = self.image.copy()
        white_overlay.fill((255, 255, 255), special_flags=pygame.BLEND_RGB_ADD)
        self.image.blit(white_overlay, (0, 0))
        self.is_flashing = True
        self.flash_timer = pygame.time.get_ticks()

    def die(self):
        self.scene.SCORE += 10
        SoundManager.play("square_death")
        self.kill()

    def check_bounds(self):
        if self.rect.bottom > 450:
            self.scene.player.lives = max(self.scene.player.lives - 1, 0)
            SoundManager.play("square_death")
            self.kill()

    def update(self, dt):
        self.position += self.velocity * (self.speed * dt / 1000)
        self.unique_behaviour(dt)
        self.rect.topleft = self.position

        self.check_bounds()

        # Flash recovery
        if self.is_flashing and pygame.time.get_ticks() - self.flash_timer > self.flash_duration:
            self.image = self.original_image
            self.mask = pygame.mask.from_surface(self.image)
            self.is_flashing = False

    def unique_behaviour(self, dt):
        pass