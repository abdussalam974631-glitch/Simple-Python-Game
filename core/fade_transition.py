import pygame
import core.utils

class FadeTransition:
    def __init__(self, width, height, fade_speed=5):
        self.surface = pygame.Surface((width, height))
        self.surface.fill((0, 0, 0))
        self.alpha = 0
        self.fade_speed = fade_speed
        if core.utils.DEV_MODE: self.fade_speed = 15
        self.fading_in = False
        self.fading_out = False
        self.done = False
        self.on_complete = None

    def start_fade_out(self, on_complete=None):
        self.fading_out = True
        self.fading_in = False
        self.alpha = 0
        self.done = False
        self.on_complete = on_complete

    def start_fade_in(self):
        self.fading_in = True
        self.fading_out = False
        self.alpha = 255
        self.done = False

    def update(self, screen):
        if self.fading_out:
            self.alpha += self.fade_speed
            if self.alpha >= 255:
                self.alpha = 255
                self.fading_out = False
                self.done = True
                if self.on_complete:
                    self.on_complete()
        elif self.fading_in:
            self.alpha -= self.fade_speed
            if self.alpha <= 0:
                self.alpha = 0
                self.fading_in = False
                self.done = True

        if self.fading_in or self.fading_out:
            self.surface.set_alpha(self.alpha)
            screen.blit(self.surface, (0, 0))
