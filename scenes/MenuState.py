from core.utils import *
import core.utils
import pygame

class MenuScene:
    def __init__(self, manager):
        self.manager = manager  # Reference to the scene manager
        self.manager.fade.start_fade_in()

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if PLAY_BTN_RECT.collidepoint(self.mouse_pos):
                    self.manager.fade.start_fade_out(on_complete=lambda:self.manager.change_scene("GameScene"))
                elif QUIT_BTN_RECT.collidepoint(self.mouse_pos):
                    core.utils.RUNNING = False

    def update(self, dt):
        pass

    def render(self, screen):
        global PLAY_BTN_HOVER_FLAG
        global QUIT_BTN_HOVER_FLAG
        
        self.mouse_pos = pygame.mouse.get_pos()
        screen.blit(BACKGROUND, (0, 0))
        if PLAY_BTN_RECT.collidepoint(self.mouse_pos): 
            screen.blit(PLAY_BTN_HOVER, PLAY_BTN_RECT)
            if not PLAY_BTN_HOVER_FLAG:
                CLICK_SOUND.play()
                PLAY_BTN_HOVER_FLAG = True
        else:
            screen.blit(PLAY_BTN, PLAY_BTN_RECT)
            if PLAY_BTN_HOVER_FLAG: PLAY_BTN_HOVER_FLAG = False
        
        if QUIT_BTN_RECT.collidepoint(self.mouse_pos):
            screen.blit(QUIT_BTN_HOVER, QUIT_BTN_RECT)
            if not QUIT_BTN_HOVER_FLAG:
                CLICK_SOUND.play()
                QUIT_BTN_HOVER_FLAG = True
        else:
            screen.blit(QUIT_BTN, QUIT_BTN_RECT)
            if QUIT_BTN_HOVER_FLAG: QUIT_BTN_HOVER_FLAG = False
        
        self.manager.fade.update(screen)