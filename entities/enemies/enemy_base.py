# entities/enemy.py
import pygame
from core.sound_man import SoundManager
from core.animation import Animation

class Enemy(pygame.sprite.Sprite):
    def __init__(self, animation, speed, health, scene):
        super().__init__()
        self.animation = Animation(animation)
        self.image = self.animation.get_frame().copy()
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
            self.original_animation = self.animation
            white_overlay = self.original_animation.get_frame().copy()
            white_overlay.fill((255, 255, 255), special_flags=pygame.BLEND_RGB_ADD)
            self.animation = Animation([white_overlay])
        self.is_flashing = True
        self.flash_timer = pygame.time.get_ticks()

    def die(self):
        self.scene.SCORE += 10
        self.scene.ui_manager.on_score_changed(self.scene.SCORE)
        SoundManager.play("square_death")
        self.kill()

    def check_bounds(self):
        if self.rect.bottom > 600:
            self.scene.player.take_damage()
            SoundManager.play("square_death")
            self.kill()

    def update(self, dt):
        self.position += self.velocity * (self.speed * dt / 1000)
        self.unique_behaviour(dt)
        self.rect.topleft = self.position

        self.animation.update(dt)
        self.image = self.animation.get_frame()
        # self.check_bounds()

        # Flash recovery
        if self.is_flashing and pygame.time.get_ticks() - self.flash_timer > self.flash_duration:
            self.animation = self.original_animation
            self.image = self.animation.get_frame()
            self.mask = pygame.mask.from_surface(self.image)
            self.is_flashing = False

    def unique_behaviour(self, dt):
        pass