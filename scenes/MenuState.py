from core.utils import *
import core.utils
from core.sound_man import SoundManager
from assets.buttons.Button import Button

class MenuScene:
    def __init__(self, manager):
        self.manager = manager
        self.manager.fade.start_fade_in()
        SoundManager.play_music("main_menu_music")

        self.buttons = [
            Button(PLAY_BTN, PLAY_BTN_HOVER, PLAY_BTN_RECT, self.start_game),
            Button(QUIT_BTN, QUIT_BTN_HOVER, QUIT_BTN_RECT, self.quit_game),
            Button(HELP_BTN, HELP_BTN_HOVER, HELP_BTN_RECT, self.help_screen)
        ]

    def handle_events(self, events):
        for btn in self.buttons:
            btn.update(events)

    def update(self, dt):
        pass

    def render(self, screen):
        screen.blit(BACKGROUND, (0, 0))
        for btn in self.buttons:
            btn.draw(screen)
        self.manager.fade.update(screen)

    def start_game(self):
        self.manager.fade.start_fade_out(
            on_complete=lambda: self.manager.change_scene("GameScene")
        )

    def help_screen(self):
        self.manager.fade.start_fade_out(
            on_complete=lambda: self.manager.change_scene("HelpScene")
        )

    def quit_game(self):
        core.utils.RUNNING = False

