import pygame
from core.sound_manager import SoundManager

class Button:
    def __init__(self, image, hover_image, rect, on_click):
        self.image = image
        self.hover_image = hover_image
        self.rect = rect
        self.on_click = on_click
        self.hovered = False

    def update(self, events):
        mouse_pos = pygame.mouse.get_pos()
        self.hovered = self.rect.collidepoint(mouse_pos)
        for e in events:
            if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1 and self.hovered:
                SoundManager.play("click")
                self.on_click()

    def draw(self, screen):
        screen.blit(self.hover_image if self.hovered else self.image, self.rect)
