import pygame
from core.utils import *
from core.ui_manager import UIManager
from core.ui_widgets import ScoreDisplay, LivesDisplay, WaveOverlay
from core.sound_man import SoundManager
from core.collision_system import CollisionSystem
from entities.player import Player
from entities.wave_manager import WaveManager


class GameScene:
    def __init__(self, manager):
        self.manager = manager
        self.mouse_pos = pygame.mouse.get_pos()
        self.manager.fade.start_fade_in()
        self.collision_system = CollisionSystem(self)
        SoundManager.play_music("game_menu_music")

        self.player = Player(self)
        self.powers = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.enemy_bullets = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group(self.player)

        self.GAME = True
        self.SCORE = 0
        self.paused = False

        self.ui_manager = UIManager(self)

        font_large = pygame.font.Font(None, 64)
        font_small = pygame.font.Font(None, 32)
        self.ui_manager.add(ScoreDisplay(font_small, (10, 10)))
        self.ui_manager.add(LivesDisplay(font_small, (10, 40)))
        self.ui_manager.add(WaveOverlay(font_large, (1000//2, 600//2)))

        self.wave_manager = WaveManager(self)
        self.wave_manager.start_wave(1)
        self.wave_manager.current_wave_number = 1


    def handle_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.paused = not self.paused
                
                if not self.paused:
                    if event.key == pygame.K_SPACE:
                        self.player.shoot(self.bullets, self.all_sprites)
            
            if not self.paused:
                pass


    def update(self, dt):
        
        if self.paused:
            return
        else:

            self.wave_manager.update(dt)
            self.collision_system.update()
            self.all_sprites.update(dt)
            self.ui_manager.update(dt)


        

    def render(self, screen):
        screen.blit(BACKGROUND, (0,0))
        self.all_sprites.draw(screen)
        self.ui_manager.render(screen)

        if self.paused:
            overlay = pygame.Surface((screen.get_width(), screen.get_height()))
            overlay.set_alpha(150)  
            overlay.fill((50, 50, 50))  
            screen.blit(overlay, (0, 0))

            font = pygame.font.Font(None, 48)
            text = font.render("Paused", True, (255, 255, 255))
            screen.blit(text, (screen.get_width()//2 - text.get_width()//2, screen.get_height()//2 - text.get_height()//2))

        self.manager.fade.update(screen)
    
    # def exit(self):
    #     if not self.GAME: return
    #     self.GAME = False
    #     self.manager.fade.start_fade_out(on_complete=lambda: self.manager.change_scene("MenuScene"))
