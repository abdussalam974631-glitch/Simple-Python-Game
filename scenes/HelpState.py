import pygame
from core.sound_manager import SoundManager
from core.utils import BACKGROUND, FONT_DUBAI

class HelpScene:
    def __init__(self, manager):
        self.manager = manager
        self.manager.fade.start_fade_in()

        self.text_lines = [
            "Controls:",
            "Arrow Keys - Move Player",
            "Space - Shoot",
            "",
            "Goal:",
            "Destroy enemies, survive as long as possible.",
            "",
            "Press ESC to return to Menu."
        ]

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                SoundManager.play("click")
                self.manager.fade.start_fade_out(
                    on_complete=lambda: self.manager.change_scene("MenuScene")
                )

    def update(self, dt):
        pass  # Help screen usually static, no updates needed.

    def render(self, screen):
        screen.blit(BACKGROUND, (0, 0))
        y = 150
        for line in self.text_lines:
            text = FONT_DUBAI.render(line, True, (255, 255, 255))
            screen.blit(text, (100, y))
            y += 40

        self.manager.fade.update(screen)
