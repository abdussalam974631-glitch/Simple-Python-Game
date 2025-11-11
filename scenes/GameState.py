import pygame
from core.utils import *
from core.sound_manager import SoundManager
from entities.player import Player
from entities.wave_manager import WaveManager


class GameScene:
    def __init__(self, manager):
        self.manager = manager  # Reference to the scene manager
        self.mouse_pos = pygame.mouse.get_pos()
        self.manager.fade.start_fade_in()
        SoundManager.play_music("game_menu_music")

        self.player = Player(self)
        self.powers = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group(self.player)

        self.GAME = True
        self.SCORE = 0
        self.paused = False
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

            hits = pygame.sprite.groupcollide(self.enemies, self.bullets, False, True,  collided=pygame.sprite.collide_mask)
            for enemy, bullets_hit in hits.items():
                for _ in bullets_hit:
                    enemy.take_damage(1)
            
            hits = pygame.sprite.groupcollide(self.powers, pygame.sprite.GroupSingle(self.player), True, False, collided=pygame.sprite.collide_mask)
            for power, x in hits.items():
                power.apply_to_player(self.player)

            self.all_sprites.update(dt)


        

    def render(self, screen):
        screen.blit(BACKGROUND, (0,0))
        self.all_sprites.draw(screen)

        text = pygame.font.Font(None, 36)
        score_text = text.render(f"Score: {self.SCORE}", True, (255, 255, 255))
        lives_text = text.render(f"Lives: {self.player.lives}", True, (255, 255, 255))
        wave_text = text.render(f"Waves: {self.wave_manager.current_wave_number}", True, (255, 255, 255))
        screen.blit(score_text, (10, 10))
        screen.blit(lives_text, (10, 40))
        screen.blit(wave_text, (10, 70))

        if self.paused:
            overlay = pygame.Surface((screen.get_width(), screen.get_height()))
            overlay.set_alpha(150)  
            overlay.fill((50, 50, 50))  
            screen.blit(overlay, (0, 0))

            font = pygame.font.Font(None, 48)
            text = font.render("Paused", True, (255, 255, 255))
            screen.blit(text, (screen.get_width()//2 - text.get_width()//2, screen.get_height()//2 - text.get_height()//2))

        self.manager.fade.update(screen)
    
    def exit(self):
        if not self.GAME: return
        self.GAME = False
        self.manager.fade.start_fade_out(on_complete=lambda: self.manager.change_scene("MenuScene"))
